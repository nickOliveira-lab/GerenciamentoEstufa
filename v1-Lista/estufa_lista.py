def cadastroPrato(nome):
    prato = [nome, 0, 0, 0, 0.0]
    return prato
def exibirPrato(prato):
    print(
        f'''{prato[0]} || Quantidade atual: {prato[1]}
Reposições: {prato[2]}
Saídas: {prato[3]}
Peso total: {prato[4]}'''
    )
def reposicao(lista, indice, enviada, pesoTotal):
    lista[indice][1] += enviada
    lista[indice][2] += 1
    lista[indice][4] += pesoTotal

def selecionarPrato(lista):
    selecionado = int(input(f'Selecione o prato: '))
    while selecionado <1 or selecionado > len(lista):
        selecionado = int(input(f'Selecione a {praca}: '))
    return  selecionado - 1

def exibirOpcoes(lista):
    contador = 1
    for prato in lista:
        print(f'{contador}. {prato[0]}')
        contador +=1

def saida(lista, indice, qtsaida):
    if qtsaida <= lista[indice][1]:
        lista[indice][1] -= qtsaida
        lista[indice][3] += qtsaida
    else:
        print('A quantidade de saída não pode ser maior que a quantidade disponível') 
        print(f'A quantidade disponível é {lista[indice][1]}')
def relatorio(estufa):
    totalReposicoes = 0
    totalSaidas = 0
    totalPeso = 0

    for praca in estufa:
        for prato in praca:
            totalReposicoes += prato[2]
            totalSaidas += prato[3]
            totalPeso += prato[4]

    return totalReposicoes, totalSaidas, totalPeso

def exportar_csv(estufa):
    totalReposicoes = 0
    totalSaidas = 0
    totalPeso = 0

    with open("relatorio.csv", "w", encoding="utf-8") as arquivo:
        
        # Cabeçalho
        arquivo.write("Praca,Prato,QuantidadeAtual,Reposicoes,Saidas,PesoTotal\n")

        for i in range(len(estufa)):
            for prato in estufa[i]:

                arquivo.write(
                    f"{i},{prato[0]},{prato[1]},{prato[2]},{prato[3]},{prato[4]}\n"
                )

                totalReposicoes += prato[2]
                totalSaidas += prato[3]
                totalPeso += prato[4]

        arquivo.write("\n")
        arquivo.write(f"TOTAL_REPOSICOES,{totalReposicoes}\n")
        arquivo.write(f"TOTAL_SAIDAS,{totalSaidas}\n")
        arquivo.write(f"TOTAL_PESO,{totalPeso:.2f}\n")

    print("CSV gerado com sucesso!")

    


# prato[0] = nome
# prato[1] = quantidade atual
# prato[2] = quantidade de reposições
# prato[3] = quantidade de saídas
# prato[4] = peso total

proteinas = []
guarnicoes = []
bases = []
saladas = []
estufa = [proteinas, guarnicoes, bases, saladas]
nomesPracas = ['Proteinas', 'Guarnições', 'Bases', 'Saladas']

while True:
    print('''===== MENU =====
1. Configurar estufa
2. Registrar reposição
3. Registrar saída
4. Ver painel
5. Encerrar dia
''')

    acao = int(input('O que você deseja fazer agora? '))

    if acao == 1:
        print('''\n===== CONFIGURAR ESTUFA =====

1. Proteínas
2. Guarnições
3. Bases
4. Saladas
''')

        praca = int(input('Selecione a praça: '))

        if praca == 1:
            print('\n===== PRAÇA DAS PROTEÍNAS =====')

            contador = 1

            for i in range(3):
                
                nome = input(f'Digite a {contador}ª proteína: ')
                
                prato = cadastroPrato(nome)

                proteinas.append(prato)
                contador += 1

            print('\nProteínas cadastradas:')
            print(proteinas)

        elif praca == 2:
            print('\n===== PRAÇA DAS GUARNIÇÕES =====')

            contador = 1

            for i in range(3):
                nome = input(f'Digite a {contador}ª guarnição: ')

                prato = cadastroPrato(nome)

                guarnicoes.append(prato)
                contador += 1

            print('\nGuarnições cadastradas:')
            print(guarnicoes)

        elif praca == 3:
            print('\n===== PRAÇA DAS BASES =====')

            contador = 1

            for i in range(6):
                nome = input(f'Digite o {contador}º item: ')

                prato = cadastroPrato(nome)

                bases.append(prato)
                contador += 1

            print('\nBases cadastradas:')
            print(bases)

        elif praca == 4:
            print('\n===== PRAÇA DAS SALADAS =====')

            contador = 1

            for i in range(7):
                nome = input(f'Digite a {contador}ª salada: ')

                prato = cadastroPrato(nome)

                saladas.append(prato)
                contador += 1

            print('\nSaladas cadastradas:')
            print(saladas)

        else:
            print('Praça não encontrada.')

    elif acao == 2: #REPOSIÇÃO
        print('''1. Proteínas
2. Guarnições
3. Bases
4. Saladas''')

        praca = int(input('Selecione a praça: '))
        pracaSelecionada = praca - 1         

        exibirOpcoes(estufa[pracaSelecionada])

        indice = selecionarPrato(estufa[pracaSelecionada])

        pesoTotal = float(input('Digite o peso total: '))
        enviada = int(input('Digite a quantidade a ser enviada: '))

        reposicao(estufa[pracaSelecionada], indice, enviada, pesoTotal)

    elif acao == 3: #SAÍDA
        print('''1. Proteínas
2. Guarnições
3. Bases
4. Saladas''')
        praca = int(input('Selecione a praça'))
        pracaSelecionada = praca - 1

        exibirOpcoes(estufa[pracaSelecionada])

        indice = selecionarPrato(estufa[pracaSelecionada])

        qtsaida = int(input('Quantos pratos vão sair: '))

        saida(estufa[pracaSelecionada], indice, qtsaida)


    elif acao == 4: #PAINEL
        print('=====PROTEÍNAS=====')
        for prato in proteinas:
            exibirPrato(prato)
        print('=====GUARNIÇÕES=====')        
        for prato in guarnicoes:
            exibirPrato(prato)
        print('=====BASES=====')
        for prato in bases:
            exibirPrato(prato)
        print('=====SALADAS=====')        
        for prato in saladas:
            exibirPrato(prato)

            


    elif acao == 5: #FECHANDO O SISTEMA
        totalReposicoes, totalSaidas, totalPeso = relatorio(estufa)
        
        print(f'Total de reposições: {totalReposicoes}')
        print(f'Total de saídas: {totalSaidas}')
        print(f'Total de Peso: {totalPeso}')
        
        for i in range(len(nomesPracas)):
            for prato in estufa[i]:
                print(nomesPracas[i], prato[0])

        exportar_csv(estufa)

        

        break

    else:
        print('Opção inválida.')