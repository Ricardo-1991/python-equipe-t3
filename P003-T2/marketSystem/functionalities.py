from utils import clear_screen

def insert_product(products):
    code = input("Informe o código do produto: ")
    name = input("Informe o nome do produto: ").capitalize()
    price = float(input("Informe o preço do produto: "))

    product = {
        'code': code,
        'name': name,
        'price': round(price, 2)
    }

    products.append(product)
    print("Produto cadastrado com sucesso!")

def delete_product(products):
    code_to_delete = input("Informe o código do produto a ser excluído: ")

    for i, product in enumerate(products):
        if product['code'] == code_to_delete:
            del products[i]
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado.")

def list_all_products(products):
    if not products:
        print("Nenhum produto cadastrado.")
        return

    sorted_products = sorted(products, key=lambda x: x['price'])

    print("\n=== Lista de Produtos ===")
    for index, product in enumerate(sorted_products, start=1):
        print(f"{index}. Código: {product['code']}, Nome: {product['name']}, Preço: R${product['price']:.2f}")

def consult_price(products):
    code_to_consult = input("Informe o código do produto para consultar o preço: ")

    for product in products:
        if product['code'] == code_to_consult:
            print(f"O preço do produto '{product['name']}' é R${product['price']:.2f}")
            return

    print("Produto não encontrado.")