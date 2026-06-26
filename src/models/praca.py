class Praca:
    def __init__(self, nome):
        self.nome = nome
        self.pratos = []

    def adicionar_prato(self, prato):
        self.pratos.append(prato)
    
    def mostrar_pratos(self):
        contador = 1
        for prato in self.pratos:
            print(f'{contador}. {prato.nome}')
            contador +=1
    
    def selecionar_prato(self):
        self.mostrar_pratos()
        selecionado = int(input(f'Selecione o prato: '))
        while selecionado <1 or selecionado > len(self.pratos):
            selecionado = int(input(f'Selecione o prato: '))
        return  self.pratos[selecionado - 1]