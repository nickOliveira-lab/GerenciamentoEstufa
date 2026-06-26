from models.estufa import Estufa
from models.praca import Praca
from models.prato import Prato

# Inicializa o objeto central do sistema
estufa = Estufa()

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

        opcao_praca = int(input('Selecione a praça: '))

        if opcao_praca == 1:
            praca = Praca('Proteínas')
        elif opcao_praca == 2:
            praca = Praca('Guarnições')
        elif opcao_praca == 3:
            praca = Praca('Bases')
        elif opcao_praca == 4:
            praca = Praca('Saladas')
        else:
            print('Opção inválida')
            continue


        quantidade = int(input('Quantos pratos deseja registrar:'))

        for i in range(quantidade):
            nome = input(f'Digite a {i+1}º prato: ')
            prato = Prato(nome)
            praca.adicionar_prato(prato)

            
        estufa.adicionar_praca(praca)
            

        print(f'praça {praca.nome} cadastrada com sucesso')


    elif acao == 2: #REPOSIÇÃO

        praca = estufa.selecionar_praca()
        prato = praca.selecionar_prato()

        pesoTotal = float(input('Digite o peso total: '))
        enviada = int(input('Digite a quantidade a ser enviada: '))

        prato.repor(enviada, pesoTotal)

    elif acao == 3: #SAÍDA
        print('''1. Proteínas
2. Guarnições
3. Bases
4. Saladas''')
        praca = estufa.selecionar_praca()
        prato = praca.selecionar_prato()

        qtsaida = int(input('Quantos pratos vão sair: '))

        prato.sair(qtsaida)


    elif acao == 4: #PAINEL
        for praca in estufa.pracas:
            print(praca.nome)
            for prato in praca.pratos:
                print(prato)
            


    elif acao == 5: #FECHANDO O SISTEMA

        estufa.resumo()
        estufa.exportar_csv()

        break

    else:
        print('Opção inválida.')