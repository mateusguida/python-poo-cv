import sqlite3
import os
from datetime import date

# Obtém o caminho absoluto do diretório onde este script Python está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o banco de dados na mesma pasta
caminho_banco = os.path.join(diretorio_script, "meubanco.db")

busca = input("Quem você está procurando? ").strip()
hoje = date.today()

# Conecta ao banco de dados utilizando o caminho exato mapeado
try:
  with sqlite3.connect(caminho_banco) as banco:
      banco.row_factory = sqlite3.Row  # Permite acessar os resultados como dicionários
      cur = banco.cursor()

      # Agora a consulta apontará para o arquivo correto
      cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

      total = 0

      for total, amigo in enumerate(cur, start=1):
          txtnasc = amigo['nascimento']
          info_nasc = ""
          if not txtnasc:
              info_nasc = "- Data de nascimento não informada."
          else:
            try:
              data = date.fromisoformat(str(txtnasc))
              japassou = (hoje.month, hoje.day) >= (data.month, data.day)
              idade = hoje.year - data.year - (0 if japassou else 1)
              info_nasc = f"nasceu em {data:%d/%m/%Y} e tem {idade} anos"
            except ValueError:
                info_nasc = "- data inválida."
          print(f"{amigo['nome']} {info_nasc}")

      print('-' * 30)
      if total == 0:
          print(f"Não encontrei ninguem com '{busca}' no nome.")
      elif total == 1:
          print(f"Encontrei apenas 1 amigo com '{busca}' no nome.") 
      else:
          print(f"Ao todo encontrei {total} amigos com '{busca}' no nome.")

except sqlite3.Error as erro:
  print(f"Ocorreu um erro ao acessar o banco de dados: {erro}")

except Exception as erro:
  print(f"Algo deu errado com o seu banco de dados: {erro}")