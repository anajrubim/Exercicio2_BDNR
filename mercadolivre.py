from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://anajrbcosta25:Aj_25042006@cluster0.ndwc6e7.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.mercadolivre


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido!")


def input_opcao(msg, opcoes):
    while True:
        valor = input(msg).upper()
        if valor in opcoes:
            return valor
        print("Opção inválida!")


def create_usuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")

    enderecos = []
    while True:
        add = input_opcao("Adicionar endereço? (S/N): ", ["S", "N"])
        if add == 'N':
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
        "enderecos": enderecos,
        "favoritos": []
    }

    try:
        db.usuario.insert_one(usuario)
        print("Usuário inserido com sucesso")
    except Exception as e:
        print("Erro:", e)


def read_usuario():
    nome = input("Nome (vazio = todos): ")
    try:
        usuarios = db.usuario.find({"nome": nome}) if nome else db.usuario.find()
        for u in usuarios:
            print(u)
    except Exception as e:
        print("Erro:", e)


def update_usuario():
    cpf = input("CPF do usuário: ")
    usuario = db.usuario.find_one({"cpf": cpf})

    if not usuario:
        print("Usuário não encontrado")
        return

    update = {}

    novo_nome = input("Novo nome: ")
    if novo_nome:
        update["nome"] = novo_nome

    novo_sobrenome = input("Novo sobrenome: ")
    if novo_sobrenome:
        update["sobrenome"] = novo_sobrenome

    if update:
        try:
            db.usuario.update_one({"cpf": cpf}, {"$set": update})
            print("Atualizado com sucesso")
        except Exception as e:
            print("Erro:", e)
    else:
        print("Nada para atualizar")


def delete_usuario():
    cpf = input("CPF: ")
    try:
        result = db.usuario.delete_one({"cpf": cpf})
        print("Quantidade deletada:", result.deleted_count)
    except Exception as e:
        print("Erro:", e)


def add_favorito():
    cpf = input("CPF do usuário: ")
    produto = input("Nome do produto: ")

    try:
        db.usuario.update_one(
            {"cpf": cpf},
            {"$addToSet": {"favoritos": produto}}
        )
        print("Favorito adicionado")
    except Exception as e:
        print("Erro:", e)


def remove_favorito():
    cpf = input("CPF do usuário: ")
    produto = input("Nome do produto: ")

    try:
        db.usuario.update_one(
            {"cpf": cpf},
            {"$pull": {"favoritos": produto}}
        )
        print("Favorito removido")
    except Exception as e:
        print("Erro:", e)


def read_favoritos():
    cpf = input("CPF do usuário: ")

    try:
        usuario = db.usuario.find_one({"cpf": cpf})

        if not usuario:
            print("Usuário não encontrado")
            return

        favoritos = usuario.get("favoritos", [])

        if favoritos:
            print("\nFavoritos:")
            for f in favoritos:
                print("-", f)
        else:
            print("Nenhum favorito cadastrado")

    except Exception as e:
        print("Erro:", e)


def create_vendedor():
    vendedor = {
        "nome": input("Nome: "),
        "sobrenome": input("Sobrenome: "),
        "email": input("Email: "),
        "cnpj": input("CNPJ: ")
    }

    try:
        db.vendedor.insert_one(vendedor)
        print("Vendedor inserido com sucesso")
    except Exception as e:
        print("Erro:", e)


def read_vendedor():
    try:
        for v in db.vendedor.find():
            print(v)
    except Exception as e:
        print("Erro:", e)


def update_vendedor():
    nome = input("Nome do vendedor: ")
    vendedor = db.vendedor.find_one({"nome": nome})

    if vendedor:
        update = {}
        novo_email = input("Novo email: ")

        if novo_email:
            update["email"] = novo_email

        if update:
            try:
                db.vendedor.update_one({"_id": vendedor["_id"]}, {"$set": update})
                print("Atualizado com sucesso")
            except Exception as e:
                print("Erro:", e)
        else:
            print("Nada para atualizar")
    else:
        print("Vendedor não encontrado")


def delete_vendedor():
    nome = input("Nome: ")

    try:
        result = db.vendedor.delete_one({"nome": nome})
        print("Quantidade deletada:", result.deleted_count)
    except Exception as e:
        print("Erro:", e)


def create_produto():
    produto = {
        "nome": input("Nome: "),
        "valor": input_float("Valor: "),
        "descricao": input("Descrição: ")
    }

    try:
        db.produto.insert_one(produto)
        print("Produto inserido com sucesso")
    except Exception as e:
        print("Erro:", e)


def read_produto():
    try:
        for p in db.produto.find():
            print(f"ID: {p['_id']} | Nome: {p['nome']} | Valor: {p['valor']}")
    except Exception as e:
        print("Erro:", e)


def update_produto():
    id_produto = input("ID do produto: ")

    try:
        produto = db.produto.find_one({"_id": ObjectId(id_produto)})
    except:
        print("ID inválido")
        return

    if produto:
        update = {}

        novo_nome = input("Novo nome: ")
        if novo_nome:
            update["nome"] = novo_nome

        novo_valor = input("Novo valor: ")
        if novo_valor:
            try:
                update["valor"] = float(novo_valor)
            except:
                print("Valor inválido")
                return

        if update:
            db.produto.update_one(
                {"_id": ObjectId(id_produto)},
                {"$set": update}
            )
            print("Atualizado")
        else:
            print("Nada para atualizar")
    else:
        print("Produto não encontrado")


def delete_produto():
    id_produto = input("ID do produto: ")

    try:
        result = db.produto.delete_one({"_id": ObjectId(id_produto)})
        print("Quantidade deletada:", result.deleted_count)
    except Exception as e:
        print("Erro:", e)


def create_compra():
    compra = {
        "cpf": input("CPF do usuário: "),
        "produto": input("Nome do produto: "),
        "valorTotal": input_float("Valor total: ")
    }

    try:
        db.compra.insert_one(compra)
        print("Compra inserida com sucesso")
    except Exception as e:
        print("Erro:", e)


def read_compra():
    try:
        for c in db.compra.find():
            print(c)
    except Exception as e:
        print("Erro:", e)


def update_compra():
    cpf = input("CPF do usuário: ")
    produto = input("Nome do produto: ")

    compra = db.compra.find_one({
        "cpf": cpf,
        "produto": produto
    })

    if compra:
        novo_valor = input("Novo valor total: ")

        try:
            novo_valor = float(novo_valor)
        except:
            print("Valor inválido")
            return

        db.compra.update_one(
            {"_id": compra["_id"]},
            {"$set": {"valorTotal": novo_valor}}
        )

        print("Compra atualizada")
    else:
        print("Compra não encontrada")


def delete_compra():
    cpf = input("CPF do usuário: ")

    try:
        result = db.compra.delete_one({"cpf": cpf})
        print("Quantidade deletada:", result.deleted_count)
    except Exception as e:
        print("Erro:", e)


while True:
    print("\n====== MENU ======")
    print("1 - CRUD Usuário")
    print("2 - CRUD Vendedor")
    print("3 - CRUD Produto")
    print("4 - CRUD Compra")
    print("5 - Favoritos")
    print("6 - Ver Favoritos")
    print("S - Sair")

    op = input_opcao("Opção: ", ["1", "2", "3", "4", "5", "6", "S"])

    if op == 'S':
        break

    if op == '5':
        print("1-Adicionar 2-Remover")
        fav = input_opcao("Escolha: ", ["1", "2"])
        if fav == '1':
            add_favorito()
        else:
            remove_favorito()
        continue

    if op == '6':
        read_favoritos()
        continue

    print("1-Create 2-Read 3-Update 4-Delete")
    sub = input_opcao("Escolha: ", ["1", "2", "3", "4"])

    if op == '1':
        if sub == '1': create_usuario()
        elif sub == '2': read_usuario()
        elif sub == '3': update_usuario()
        elif sub == '4': delete_usuario()

    elif op == '2':
        if sub == '1': create_vendedor()
        elif sub == '2': read_vendedor()
        elif sub == '3': update_vendedor()
        elif sub == '4': delete_vendedor()

    elif op == '3':
        if sub == '1': create_produto()
        elif sub == '2': read_produto()
        elif sub == '3': update_produto()
        elif sub == '4': delete_produto()

    elif op == '4':
        if sub == '1': create_compra()
        elif sub == '2': read_compra()
        elif sub == '3': update_compra()
        elif sub == '4': delete_compra()
