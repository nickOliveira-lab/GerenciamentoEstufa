class Prato:
    def __init__(self, nome):
        self.nome = nome
        self.qtAtual = 0
        self.reposicoes = 0
        self.saidas = 0
        self.pesoTotal = 0.0

    def repor(self, enviada, pesoTotal):
            self.qtAtual += enviada
            self.reposicoes += 1
            self.pesoTotal += pesoTotal
        
    def sair(self, quantidade):
            if quantidade <= self.qtAtual:
                self.qtAtual -= quantidade
                self.saidas += quantidade
            else:
                print('A quantidade de saída não pode ser maior que a quantidade disponível') 
                print(f'A quantidade disponível é {self.qtAtual}')
        
    def __str__(self):
            return(f'''Nome: {self.nome}
Quantidade atual: {self.qtAtual}
Reposições: {self.reposicoes}
Saídas: {self.saidas}
Peso total: {self.pesoTotal}
-----------------------------''')