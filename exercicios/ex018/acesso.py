import sqlite3
import os

# Obtém o caminho absoluto do diretório onde este script Python está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o banco de dados na mesma pasta
caminho_banco = os.path.join(diretorio_script, "meubanco.db")

busca = input("Quem você está procurando? ").strip()

# Conecta ao banco de dados utilizando o caminho exato mapeado
try:
  with sqlite3.connect(caminho_banco) as banco:
      banco.row_factory = sqlite3.Row  # Permite acessar os resultados como dicionários
      cur = banco.cursor()

      # Agora a consulta apontará para o arquivo correto
      cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

      # Exemplo para testar a leitura
      # resultados = cur.fetchall() # comando ruim para bases de dados grandes, pois carrega tudo na memória
      # print(resultados)

      total = 0

      for total, amigo in enumerate(cur, start=1):
          print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")

      print(f"Total de amigos encontrados: {total}")

except sqlite3.Error as erro:
  print(f"Ocorreu um erro ao acessar o banco de dados: {erro}")

except Exception as erro:
  print(f"Algo deu errado com o seu banco de dados: {erro}")

# Fechando a conexão com o banco de dados (para versão sem usar o with)
# cur.close()
# banco.close()