class Impressora:
    modelo = "Epson"

    def __init__(self, numero_folhas):
        self.numero_folhas = numero_folhas

    def imprimir_folha(self):
        print("folha impressa")

    def imprimir_livro(self, paginas):
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas -= 1

    @classmethod
    def print_modelo(cls):
        print(cls.modelo)


    def print_modelo_instancia(self):
        print(self.modelo)


impressora = Impressora(15)

impressora.imprimir_folha()

impressora.imprimir_livro(10)

Impressora.print_modelo()

impressora.print_modelo_instancia()
