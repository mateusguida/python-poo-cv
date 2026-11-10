import sqlite3

NOME_BANCO = "exercicios/ex019/cadastro.db"

def criar_banco() -> bool:
    try:
      with sqlite3.connect(NOME_BANCO) as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL);")
        return True

    except sqlite3.Error as e:
        print(f"[ERRO] Ocorreu um erro ao criar o banco de dados: {e}") 

def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Alice", "1.65"),
        ("2", "Bob", "1.80"),
        ("3", "Charlie", "1.75"),
        ("4", "Diana", "1.60"),
        ("5", "Ethan", "1.85")
    ]

    try:
      with sqlite3.connect(NOME_BANCO) as db:
         cursor = db.cursor()
         cursor.executemany("INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?);", cad_pessoas)
         db.commit()
         print("\nCadastro em massa realizado com sucesso!")
    except sqlite3.Error as e:
        print(f"[ERRO] Ocorreu um erro ao realizar o cadastro em massa: {e}")

def cadastrar_pessoa() -> bool:
    print("\n ==== NOVO CADASTRO DE PESSOA ====")

    # Leitura e validação dos dados
    val_nome = input("Nome: ").strip()
    if not val_nome:
        print("\n[ERRO] O nome não pode ser vazio!")
        return False

    val_altura = input("Altura (em metros): ").strip().replace(",", ".")
    if not val_altura:
        print("\n[ERRO] A altura não pode ser vazia!")
        return False
    try:
        val_altura = float(val_altura)
        if val_altura <= 0.30 or val_altura >= 3.00:
            print("\n[ERRO] Valor incoerente para altura!")
            return False
    except ValueError:
        print("\n[ERRO] A altura deve ser um número válido!")
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?);", (val_nome, val_altura))
            db.commit()
            print(f"\nCadastro de {val_nome} realizado com sucesso!")
            return True
    except sqlite3.Error as e:
        print(f"[ERRO] Ocorreu um erro ao cadastrar a pessoa: {e}")
        return False

def listar_pessoas() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_por_nome() -> bool:
    pass