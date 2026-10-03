from functions import *

## ----- MENU ----- ##

nuvem = input("A LISTA JÁ ESTÁ NA NUVEM? S/N: ").lower()

if nuvem == "s":
    lista = carregar()

elif nuvem == "n":
    entrada = input("DIGITE SUA LISTA DE NOMES: ")
    lista = []

    for pessoa in entrada.split(";"):
        dados = pessoa.split(",")

        if len(dados) != 3:
            print("CADASTRO INVÁLIDO!")
            continue

        nome = dados[0]
        cpf = dados[1]
        estado = dados[2]

        cpf_existe = False

        for pessoa in lista:
            if cpf == pessoa[1]:
                print("CPF JÁ EXISTENTE!")
                cpf_existe = True
                break

        if not cpf_existe:
            lista.append([nome, cpf, estado])

else:
    print("OPÇÃO INVÁLIDA")
    lista = []


## ----- MENU PRINCIPAL ----- ##

while True:

    print("\n--- OPÇÕES ---")
    print("1 - BUSCAR")
    print("2 - REMOVER")
    print("3 - ADICIONAR")
    print("4 - MOSTRAR")
    print("5 - ORDEM ALFABÉTICA")
    print("6 - QUANTAS PESSOAS TEM NA LISTA")
    print("7 - SEPARAR POR ESTADO")
    print("8 - SALVAR LISTA")
    print("9 - EDITAR LISTA")
    print("10 - PAINEL DE DADOS")
    print("0 - SAIR")

    valor = int(input("DIGITE SUA OPÇÃO: "))

    match valor:

        case 1:
            buscar(lista)

        case 2:
            remove(lista)

        case 3:
            add(lista)

        case 4:
            mostrar(lista)

        case 5:
            alfabetica(lista)

        case 6:
            total(lista)

        case 7:
            uf(lista)

        case 8:
            save(lista)

        case 9:
            editar(lista)

        case 10:
            painel(lista)

        case 0:
            sair()
            break

        case _:
            print("OPÇÃO INVÁLIDA")
