from crud import *

def exibir_menu():
    print("\n" + "=" * 30)
    print("      SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)

def main():

    if not criar_banco():
        print("\n[ERRO] Não foi possível criar o banco de dados. Encerrando o sistema...")
        raise SystemExit
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1": # Cadastrar pessoa
                if not cadastrar_pessoa():
                  print("\n[ERRO] Não foi possível cadastrar a pessoa.")

            case "2": # Listar pessoas
                if not listar_pessoas():
                    print("\n[ERRO] Não foi possível listar as pessoas.")

            case "3": # Atualizar pessoa
                if not atualizar_pessoa():
                    print("\n[ERRO] Não foi possível atualizar a pessoa.")

            case "4": # Excluir pessoa
                if not excluir_pessoa():
                    print("\n[ERRO] Não foi possível excluir a pessoa.")

            case "5": # Busca por nome
                if not buscar_por_nome():
                    print("\n[ERRO] Não foi possível buscar a pessoa pelo nome.")

            case "0": # Sair
                print("\nEncerrando o sistema...")
                break

            case _: # Opção inválida
                print("\n[ERRO] Opção inválida! Escolha um valor entre 0 e 5!")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()