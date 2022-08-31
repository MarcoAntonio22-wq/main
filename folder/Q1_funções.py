#verificações

def verificar_existêcia_CPF(dic, CPF):
    if dic.get(CPF) == None:
        return False
    else:
        return True

def verificar_existência_placa(dic, placa):
    lista = f'{dic.values()}'
    existência = lista.find(placa)
    if existência == -1:
        return False
    else:
        return True

def verificar_atividade_cliente(dic,CPF):
    forma_str = str(dic.get(CPF))
    if forma_str[29:30] == '0':
        return False
    elif forma_str[29:30] == '1':
        return True

def verivicar_existência_reserva(dic,CPF):
    forma_str = str(dic.get(CPF))
    if forma_str[31] == '0':
        return False
    if forma_str[31] == '1':
        return True

#formatações

def formatar_relatório_vagas(str):
    return f'nome:{str[8:28]} / placa:{str[0:7]}'

def formatar_relatório_clientes_atívos(CPF, str):
    return f'nome:{str[8:28]} / CPF:{CPF} / placa do carro:{str[0:7]}'

#manipulação do arquivo txt

def salvar_arq(dic):
    with open('cadastros.txt', 'w') as arq:
        lista = []
        lista_final = []
        for i in dic.keys():
            lista.append(i)
        for j in range(len(lista)):
            info_cliente = dic.get(lista[j])
            lista_final.append(f'{lista[j]},{info_cliente}')
        for h in lista_final:
            arq.write(f'{h}\n')

def ler_arquivo():
    try:
        dic1 = {}
        with open('cadastros.txt', 'r') as arq:
            lista = []
            for linha in arq:
                dic1[linha[0:11]] = linha[12:44]
        return dic1
    except FileNotFoundError:
        dic2 = {}
        return dic2

def leitura_vagas_restantes(dic,vagas_totais):
    lista1 = []
    lista_final = []
    for i in dic.values():
        lista1.append(i)
    for j in range(len(lista1)):
        linha = str(lista1[j])
        if linha[31] == '0':
            lista1.append(j+1)
        elif linha[31] == '1':
            lista_final.append(linha)
    vagas_restantes = (vagas_totais-len(lista_final))
    return vagas_restantes
