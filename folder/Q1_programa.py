import Q1_funções

#[0:7] placa do carro
#[8:28] nome do cliente
#[29:30] atívo ou inatívo
#[31] reserva de vaga

vagas_totais = 20
clientes = Q1_funções.ler_arquivo()
vagas_restantes = Q1_funções.leitura_vagas_restantes(clientes, vagas_totais)
opção = 1
while opção != 0:
    print()
    print('bom dia, o que deseja fazer?')
    print()
    print('1-cadastrar cliente')
    print('2-alugar uma vaga')
    print('3-relatório de vagas')
    print('4-relatório de clientes ativos')
    print('0-sair')
    print()
    try:
        opção = int(input('digite o número correspondente a opção desejada'))
    except:
        print('dígito inválido')

    if (opção == 1):
        try:
            CPF_cliente = input('qual o CPF do cliente?(somente números)')
            assert len(CPF_cliente) == 11
            if Q1_funções.verificar_existêcia_CPF(clientes, CPF_cliente) == True:
                print()
                print('CPF já cadastrado!')
            else:
                nome_cliente = input('qual o nome do cliente?(primeiro nome apenas[máx. 20 caractéres])')
                if len(nome_cliente) > 20:
                    print()
                    print('limíte de caracteres exedido!')
                else:
                    nome_cliente_str = str(nome_cliente).ljust(20)
                    placa_cliente = input('qual a placa do carro?(apenas letras e números)')
                    assert len(placa_cliente) == 7
                    if Q1_funções.verificar_existência_placa(clientes, placa_cliente) == True:
                        print()
                        print('placa já cadastrada!')
                    else:
                        status_cliente = int(input('cliente ativo(1) ou inativo(0)?'))
                        if status_cliente == 1 or status_cliente == 0:
                            clientes[CPF_cliente] = f'{placa_cliente},{nome_cliente_str},{status_cliente},{0}'
                            clientes_str = str(clientes.get(CPF_cliente))
                            print()
                            print('cliente cadastrado.')
                        else:
                            print()
                            print('dígito inválido!')

        except AssertionError:
            print()
            print('informação inválida ou incorreta!')

    elif (opção == 2):
        if vagas_restantes <=0:
            print('vagas esgotadas!')
        else:
            CPF_cliente = input('informe o CPF')
            if Q1_funções.verificar_existêcia_CPF(clientes, CPF_cliente) == False:
                print('CPF não cadastrado!')
            else:
                if Q1_funções.verificar_atividade_cliente(clientes,CPF_cliente) == False:
                    print('cliente inatívo!')
                elif Q1_funções.verificar_atividade_cliente(clientes, CPF_cliente) == True:
                    if Q1_funções.verivicar_existência_reserva(clientes, CPF_cliente) == True:
                        print('cliente já possui vaga reservada!')
                    elif Q1_funções.verivicar_existência_reserva(clientes,CPF_cliente) == False:
                        inf_cliente = str(clientes.get(CPF_cliente))
                        clientes[CPF_cliente] = f'{inf_cliente[0:7]},{inf_cliente[8:28]},{inf_cliente[29:30]},1'
                        print('vaga reservada.')
                        vagas_restantes -= 1
    elif (opção == 3):
        lista1 = []
        lista_final = []
        for i in clientes.values():
            lista1.append(i)
        for j in range(len(lista1)):
            linha = str(lista1[j])
            if linha[31] == '0':
                lista1.append(j+1)
            elif linha[31] == '1':
                lista_final.append(Q1_funções.formatar_relatório_vagas(linha))
        for h in lista_final:
            print(h)
        vagas_restantes = (vagas_totais-len(lista_final))
        print(f'vagas restantes: {vagas_restantes}')

    elif (opção == 4):
        lista = []
        lista_final = []
        for i in clientes.keys():
            lista.append(i)
        for j in range(len(lista)):
            info_cliente = clientes.get(lista[j])
            if info_cliente[29:30] == '1':
                CPF_cliente = lista[j]
                lista_final.append(Q1_funções.formatar_relatório_clientes_atívos(CPF_cliente, info_cliente))
        for h in lista_final:
            print(h)
    elif(opção == 0):
        Q1_funções.salvar_arq(clientes)
        break
    elif(opção != 0):
        print()
        print('dígito inválido')
