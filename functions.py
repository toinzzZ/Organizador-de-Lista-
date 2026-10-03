import json
## ----- FUNÇOES MENU ------- ##
def buscar(lista):
    nome = input("QUE NOME VOCÊ QUER BUSCAR? ")

    for pessoa in lista:
        if nome.lower() in pessoa[0].lower():
            print("O NOME ESTÁ NA LISTA!")
            return
        elif nome == pessoa[1]:
            print("SEU CPF ESTÁ NA LISTA!")
            return
    print("NÃO NÃO ESTÁ NA LISTA")

def remove(lista):
    busca = input("QUE NOME OU CPF VOCÊ QUER REMOVER? ")

    for pessoa in lista:
        if busca.lower() == pessoa[0].lower() or busca == pessoa[1]:
            lista.remove(pessoa)
            print("PESSOA REMOVIDA!")
            return

    print("PESSOA NÃO EXISTENTE")

def add(lista):
    novapessoa = input("O QUE VOCÊ QUER ADICIONAR? ")
    for pessoa in novapessoa.split(";"):
        dados = pessoa.split(",")

        nome = dados[0]
        cpf = dados[1]
        estado = dados[2]

        lista.append([nome, cpf, estado])
    print(lista)

def mostrar(lista):  
    print("\n" + "=" * 50)
    print("              PESSOAS CADASTRADAS")
    print("=" * 50)

    for numero, pessoa in enumerate(lista, start=1):
        print(f"\n[{numero}]")
        print(f"Nome : {pessoa[0]}")
        print(f"CPF  : {pessoa[1]}")
        print(f"UF   : {pessoa[2]}")
        print("-" * 50)

def alfabetica(lista):
    lista.sort()
    print(lista)

def total(lista):
     print(len(lista))

def uf(lista):
    estado = input("DIGITE O ESTADO: ")

    for pessoa in lista:
        if estado.lower() == pessoa[2].lower():
            print(f"NOME: {pessoa[0]}")
            print(f"CPF: {pessoa[1]}")
            print(f"UF: {pessoa[2]}")
            print("----------------")
def save(lista):
    with open("bd.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii= False, indent= 4 )

    print("DADOS SALVOS!")

def editar(lista):
    busca = input("DIGITE O NOME OU CPF PARA EDITAR:")
    for pessoa in lista:
        if busca.lower() == pessoa[0].lower() or busca.lower() == pessoa[1].lower():
            print("\nPESSOA ENCONTRADA!")
            print(f"Nome: {pessoa[0]}")
            print(f"CPF: {pessoa[1]}")
            print(f"UF: {pessoa[2]}")

            print("\n--- O QUE DESEJA EDITAR? ---")
            print("1 - NOME")
            print("2 - CPF")
            print("3 - UF")
            print("0 - CANCELAR")

            opcao = int(input("QUAL OPÇAO VOCE QUER?"))

            if opcao == 1:
                novo_nome =  input("QUAL É O NOVO NOME?")
                pessoa[0] = novo_nome

            elif opcao == 2:
                novo_cpf = input("QUAL NOVO CPF?")
                pessoa[1] = novo_cpf
            elif opcao == 3:
                novo_uf = input("QUAl É O NOVO ESTADDO?")
                pessoa[2] = novo_uf

            elif opcao == 0:
                print("CANCELANDO...")
                return
            else:
                print("OPÇÃO ERRADA")
                return
            
        print("DADOS ALTERADOS COM SUCESSO")
        save(lista)
        return
    
    print("PESSOA NÃO ENCONTRADA!")

def sair():
    print("SAINDO...")

##------ FINAL ------- ##

##------- VERIFICAÇAO --------- ##
def carregar():
    try:
        with open("bd.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        print("DADOS CARREGADOS!")
        return dados

    except FileNotFoundError:
        print("ARQUIVO bd.json NÃO ENCONTRADO.")
        return []

## ------ FINAL ------ ##

## ------ DADOS ------ ##

def totalpessoas(lista):
    return len(lista)

def pessoas_estado(lista):
    estados = {}

    for pessoa in lista:
        estado = pessoa[2]

        if estado in estados:
            estados[estado] += 1

        else:
            estados[estado] = 1

    return estados

def painel(lista):
    print("=" * 40)
    print("        PAINEL DE DADOS")
    print("=" * 40)

    print(f"Total de pessoas: {totalpessoas(lista)}")

    print("\nPESSOAS POR ESTADO:")

    estados = pessoas_estado(lista)

    for estado, quantidade in estados.items():
        print(f"{estado}: {quantidade}")

    print("=" * 40)

## ------- FINISH ------ ##
