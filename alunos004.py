def cria_cadastro(nome, sobrenome, idade, cpf):
    return {'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'cpf': cpf}

lista_alunos = []
opcao = 3

while opcao != 0:
    print('='*30)   
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - listar todos')
    print('='*30)   
    opcao = input('Digite uma opção')

    if opcao == 1:
        nome = input('nome: ')
        sobrenome = input('sobrenome: ')
        idade = int(input('idade: '))
        cpf = input('cpf: ')
        aluno = cria_cadastro(nome, sobrenome, idade, cpf)
        for a in lista_alunos:
            if a['cpf'] == cpf:
                verificador = 1
                print('cpf já cadastrado')
        if verificador == 0:
            lista_alunos.append(aluno)
    elif opcao == 2:
        for i in lista_alunos:
            print(i)





aluno = cria_cadastro('luquinhas', 'calminho', 12, '03994875629')

print('='*30)    
