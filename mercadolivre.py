from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anajrbcosta25:Aj_25042006@cluster0.ndwc6e7.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.mercadolivre

def create_usuario():
    print("\n--- Criar Usuário ---")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")

    enderecos = []
    while True:
        add = input("Adicionar endereço? (S/N): ").upper()
        if add != 'S':
            break

        endereco = {
            "rua": input("Rua: "),
            "numero": input("Número: "),
            "cidade": input("Cidade: "),
            "estado": input("Estado: "),
            "cep": input("CEP: ")
        }
        enderecos.append(endereco)

    usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": cpf,
        "enderecos": enderecos
    }

    db.usuario.insert_one(usuario)
    print("Usuário inserido com sucesso")

def read_usuario():
    print("\n--- Buscar Usuário ---")
    nome = input("Nome (vazio = todos): ")

    if nome:
        usuarios = db.usuario.find({"nome": nome})
    else:
        usuarios = db.usuario.find()

    for u in usuarios:
        print(u)

def update_usuario():
    print("\n--- Atualizar Usuário ---")
    nome = input("Nome do usuário: ")

    usuario = db.usuario.find_one({"nome": nome})

    if not usuario:
        print("Usuário não encontrado")
        return

    print("Atual:", usuario)

    novo_nome = input("Novo nome: ")
    if novo_nome:
        usuario["nome"] = novo_nome

    novo_sobrenome = input("Novo sobrenome: ")
    if novo_sobrenome:
        usuario["sobrenome"] = novo_sobrenome

    db.usuario.update_one({"_id": usuario["_id"]}, {"$set": usuario})
    print("Atualizado com sucesso")

def delete_usuario():
    print("\n--- Deletar Usuário ---")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")

    result = db.usuario.delete_one({"nome": nome, "sobrenome": sobrenome})
    print("Quantidade deletada:", result.deleted_count)

def create_vendedor():
    print("\n--- Criar Vendedor ---")
    vendedor = {
        "nome": input("Nome: "),
        "sobrenome": input("Sobrenome: "),
        "email": input("Email: "),
        "cnpj": input("CNPJ: ")
    }

    db.vendedor.insert_one(vendedor)
    print("Vendedor inserido com sucesso")

def read_vendedor():
    vendedores = db.vendedor.find()
    for v in vendedores:
        print(v)

def update_vendedor():
    nome = input("Nome do vendedor: ")
    vendedor = db.vendedor.find_one({"nome": nome})

    if vendedor:
        novo_email = input("Novo email: ")
        if novo_email:
            vendedor["email"] = novo_email

        db.vendedor.update_one({"_id": vendedor["_id"]}, {"$set": vendedor})
        print("Atualizado com sucesso")
    else:
        print("Vendedor não encontrado")

def delete_vendedor():
    nome = input("Nome: ")
    result = db.vendedor.delete_one({"nome": nome})
    print("Quantidade deletada:", result.deleted_count)

def create_produto():
    print("\n--- Criar Produto ---")
    produto = {
        "nome": input("Nome: "),
        "valor": float(input("Valor: ")),
        "descricao": input("Descrição: ")
    }

    db.produto.insert_one(produto)
    print("Produto inserido com sucesso")

def read_produto():
    produtos = db.produto.find()
    for p in produtos:
        print(p)

def update_produto():
    nome = input("Nome do produto: ")
    produto = db.produto.find_one({"nome": nome})

    if produto:
        novo_valor = input("Novo valor: ")
        if novo_valor:
            produto["valor"] = float(novo_valor)

        db.produto.update_one({"_id": produto["_id"]}, {"$set": produto})
        print("Atualizado com sucesso")
    else:
        print("Produto não encontrado")

def delete_produto():
    nome = input("Nome: ")
    result = db.produto.delete_one({"nome": nome})
    print("Quantidade deletada:", result.deleted_count)

def create_compra():
    print("\n--- Criar Compra ---")
    compra = {
        "usuario": input("Nome do usuário: "),
        "produto": input("Nome do produto: "),
        "valorTotal": float(input("Valor total: "))
    }

    db.compra.insert_one(compra)
    print("Compra inserida com sucesso")

def read_compra():
    compras = db.compra.find()
    for c in compras:
        print(c)

def update_compra():
    usuario = input("Nome do usuário: ")
    compra = db.compra.find_one({"usuario": usuario})

    if compra:
        novo_valor = input("Novo valor total: ")
        if novo_valor:
            compra["valorTotal"] = float(novo_valor)

        db.compra.update_one({"_id": compra["_id"]}, {"$set": compra})
        print("Atualizado com sucesso")
    else:
        print("Compra não encontrada")

def delete_compra():
    usuario = input("Nome do usuário: ")
    result = db.compra.delete_one({"usuario": usuario})
    print("Quantidade deletada:", result.deleted_count)

while True:
    print("MENU")
    print("1 - CRUD Usuário")
    print("2 - CRUD Vendedor")
    print("3 - CRUD Produto")
    print("4 - CRUD Compra")
    print("S - Sair")

    op = input("Opção: ").upper()

    if op == 'S':
        break

    if op == '1':
        print("\n1-Create 2-Read 3-Update 4-Delete")
        sub = input("Escolha: ")

        if sub == '1': create_usuario()
        elif sub == '2': read_usuario()
        elif sub == '3': update_usuario()
        elif sub == '4': delete_usuario()

    elif op == '2':
        print("\n1-Create 2-Read 3-Update 4-Delete")
        sub = input("Escolha: ")

        if sub == '1': create_vendedor()
        elif sub == '2': read_vendedor()
        elif sub == '3': update_vendedor()
        elif sub == '4': delete_vendedor()

    elif op == '3':
        print("\n1-Create 2-Read 3-Update 4-Delete")
        sub = input("Escolha: ")

        if sub == '1': create_produto()
        elif sub == '2': read_produto()
        elif sub == '3': update_produto()
        elif sub == '4': delete_produto()

    elif op == '4':
        print("\n1-Create 2-Read 3-Update 4-Delete")
        sub = input("Escolha: ")

        if sub == '1': create_compra()
        elif sub == '2': read_compra()
        elif sub == '3': update_compra()
        elif sub == '4': delete_compra()