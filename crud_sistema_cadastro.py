usuarios = []

# Linha
def linha(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)
    

# Cadastro
def cadastrar():
    nome = input("Digite o nome: ")
    usuarios.append(nome)
    print("Usuário cadastrado!")

# Lista
def listar():
    if not usuarios:
        print("Lista vazia..")
        return

    for i, usuario in enumerate(usuarios):
        print(f"{i} - {usuario}")

# Atualizar
def atualizar():
    listar()
    indice = int(input("Digite o índice para atualizar: "))

    if 0 <= indice < len(usuarios):
        novo_nome = input("Novo nome: ")
        usuarios[indice] = novo_nome
        print("Atualizado com sucesso!")
    else:
        print("Índice inválido.")

# Remover
def remover():
    listar()
    indice = int(input("Digite o índice para remover: "))

    if 0 <= indice < len(usuarios):
        usuarios.pop(indice)
        print("Removido com sucesso!")
    else:
        print("Índice inválido.")

# Menu
while True:
    linha('SISTEMA DE CADASTRO')
    print(""" 
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Remover
5 - Sair
""")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")