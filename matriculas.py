opcao = None
lista_alunos = []


def matricular_aluno():
    aluno = {
        "Nome": "",
        "Data de Nascimento": "",
        "Idade": 0,
        "Nome da mãe": "",
        "CPF": "",
        "Telefone": "",
        "Turno": ""
    }

    print("Preencha os campos abaixo para cadastrar um(a) aluno(a):")
    for chave in aluno:
        aluno[chave] = input(chave + ":")

    lista_alunos.append(aluno)
    return


def listar_alunos():
    turno = input("Qual turno? Manhã, tarde ou integral?").lower()
    while turno not in ["manhã", "tarde", "integral"]:
        turno = input("Turno inválido. Manhã, tarde ou integral?").lower()

    '''
    alunos_por_turno = [aluno for aluno in lista_alunos if aluno['Turno'].lower() == turno]
    for elemento in alunos_por_turno:
        for chave in elemento:
            print(f"{chave}: {elemento[chave]}")
        print("-"*20)
    '''
    for elemento in lista_alunos:
        if elemento["Turno"].lower() == turno:
            for chave in elemento:
                print(f"{chave}: {elemento[chave]}")
            print("-" * 20)

    return


while opcao != "3":

    if opcao == "1":
        matricular_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        break

    print("{:^30}".format("MATRICULA ESCOLAR"))
    print("Digite o número da opção desejada:")
    print("1- Matricular aluno(a)")
    print("2- Lista dos alunos matriculados por turno")
    print("3- Sair")
    opcao = input()

    while opcao not in ["1", "2", "3"]:
        opcao = input("Opção inválida. 1, 2 ou 3?")
