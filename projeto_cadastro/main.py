from funcoes import *

usuarios = carregar_dados()

while True:
    print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Remover
5 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar(usuarios)
    elif opcao == "2":
        listar(usuarios)
    elif opcao == "3":
        atualizar(usuarios)
    elif opcao == "4":
        remover(usuarios)
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")