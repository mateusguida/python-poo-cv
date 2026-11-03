import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco() -> bool:
    try:
      with sqlite3.connect(NOME_BANCO) as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL);")
        return True

    except sqlite3.Error as e:
        print(f"[ERRO] Ocorreu um erro ao criar o banco de dados: {e}") 

def cadastrar_pessoa() -> bool:
   pass

def listar_pessoas() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_por_nome() -> bool:
    pass