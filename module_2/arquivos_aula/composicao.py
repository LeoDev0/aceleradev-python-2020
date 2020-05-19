class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.num_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f"Fechando o pedido: {self.num_pedido}")
        print(f"Valor do carrinho: {self.valor_carrinho}")
        print(f"Nome cliente: {self.cliente.nome}")
        print("Obrigado pela compra")


cliente = Cliente("Élysson", "123456")

televisao = Produto("Televisão", 1000.90)
maquina_cafe = Produto("Máquina de café", 89.80)

produtos = [televisao, maquina_cafe]

carrinho = CarrinhoCompras(cliente, produtos)

teclado = Produto("Teclado Mecanico", 175.20)
carrinho.adicionar_produto(teclado)

carrinho.remover_produto(televisao)

print(carrinho.valor_carrinho)
carrinho.fechar_carrinho()
