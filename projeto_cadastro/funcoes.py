import json

ARQUIVO = "dados.json"

############## CARREGAR JSON ##############

def carregar_dados():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

############## SALVA OS DADOS ##############

def salvar_dados(usuarios):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

############## CADASTRO ##############

def cadastrar(usuarios):
    nome = input("Digite o nome: ")
    usuarios.append(nome)
    salvar_dados(usuarios)
    print("Usuário cadastrado!")

############## LISTA ##############

def listar(usuarios):
    if not usuarios:
        print("Lista vazia.")
        return

    for i, usuario in enumerate(usuarios):
        print(f"{i} - {usuario}")

############## ATUALIZAR ##############

def atualizar(usuarios):
    listar(usuarios)
    try:
        indice = int(input("Índice para atualizar: "))
        usuarios[indice] = input("Novo nome: ")
        salvar_dados(usuarios)
    except (ValueError, IndexError):
        print("Entrada inválida.")

############## REMOVER ##############

def remover(usuarios):
    listar(usuarios)
    try:
        indice = int(input("Índice para remover: "))
        usuarios.pop(indice)
        salvar_dados(usuarios)
    except (ValueError, IndexError):
        print("Entrada inválida.")