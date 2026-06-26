import csv

class ExportadorService:
    @staticmethod
    def para_csv(estufa, caminho_arquivo='relatorio_estufa.csv'):
        """
        Recebe um objeto Estufa e exporta seus dados para um arquivo CSV.
        Permite mudar o caminho onde o arquivo será salvo.
        """
        with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Praça', 'Prato', 'Qtd Atual', 'Reposições', 'Saídas', 'Peso Total'])
            
            for praca in estufa.pracas:
                for prato in praca.pratos:
                    writer.writerow([
                        praca.nome,
                        prato.nome,
                        prato.qtAtual,
                        prato.reposicoes,
                        prato.saidas,
                        prato.pesoTotal
                    ])
        print(f"Relatório CSV gerado com sucesso em: {caminho_arquivo}")