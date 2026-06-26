import csv
class Estufa:
    def __init__(self):
        self.pracas = []
    
    def adicionar_praca(self, praca):
        self.pracas.append(praca)

    def mostrar_pracas(self):
        contador = 1
        for praca in self.pracas:
            print(f'{contador}. {praca.nome}')
            contador += 1
    
    def selecionar_praca(self):
        self.mostrar_pracas()
        selecionado = int(input(f'Selecione a praca: '))
        while selecionado <1 or selecionado > len(self.pracas):
            selecionado = int(input(f'Selecione a praca: '))
        return  self.pracas[selecionado - 1]
    
    def resumo(self):
        totalReposicoes = 0
        totalSaidas = 0
        pesoTotal = 0


        for praca in self.pracas:
            for prato in praca.pratos:
                totalReposicoes += prato.reposicoes
                totalSaidas += prato.saidas
                pesoTotal += prato.pesoTotal

        print("\n===== RESUMO DO DIA =====")
        print(f"Reposições: {totalReposicoes}")
        print(f"Saídas: {totalSaidas}")
        print(f"Peso total: {pesoTotal}")
        print("=========================\n")
    
    def exportar_csv(self):
        with open('relatorio_estufa.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Praça', 'Prato', 'Qtd Atual', 'Reposições', 'Saídas', 'Peso Total'])
            for praca in self.pracas:
                for prato in praca.pratos:
                    writer.writerow([
                        praca.nome,
                        prato.nome,
                        prato.qtAtual,
                        prato.reposicoes,
                        prato.saidas,
                        prato.pesoTotal])