from functionalities import *

def main():
    products = []

    while True:
        clear_screen()
        print("==== Supermercado ====")
        print("1. Inserir Produto")
        print("2. Excluir Produto")
        print("3. Listar Todos os Produtos")
        print("4. Consultar Preço")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            insert_product(products)
        elif choice == '2':
            delete_product(products)
        elif choice == '3':
            list_all_products(products)
        elif choice == '4':
            consult_price(products)
        elif choice == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()