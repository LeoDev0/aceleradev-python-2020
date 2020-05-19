class Impressora:
    @staticmethod
    def ligar_para_suporte():
        print("Liguei para o suporte")

    @classmethod
    def deu_problema_na_impressora(cls):
        print("analisando problema")
        cls.ligar_para_suporte()

    def imprimir(self):
        print("imprimindo pagina 1")
        self.ligar_para_suporte()


Impressora.ligar_para_suporte()

Impressora.deu_problema_na_impressora()

impressora = Impressora()

impressora.imprimir()
