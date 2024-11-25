from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        if isinstance(numero, int):
            self.__numero = numero
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(tipo, TipoPedido):
            self.__tipo = tipo
        self.__itens = []


    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero
        ...

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    '''
    Inclui um novo item na lista de itens do pedido.
    Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    Retornar o item incluido em caso de sucesso e None em caso
    de item duplicado.
    '''

    def inclui_item_pedido(self, codigo: int, descricao: str, preco: float):
        # Verifica se o item já existe na lista de itens
        for item in self.__itens:
            if item.codigo == codigo:
                return None  # Se encontrar item com o mesmo código, retorna None

        # Cria um novo item e adiciona à lista
        item = ItemPedido(codigo, descricao, preco)
        self.__itens.append(item)  # Adiciona o item à lista privada
        return item  # Retorna o item incluído


    '''
    Exclui um item do pedido e retorna o item excluido
    Caso o item nao exista, retorne None
    '''
    def exclui_item_pedido(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                self.itens.remove(item)
                return item
        return None

    '''
    Deve calcular o valor total do pedido, considerando um custo
    adicional pela distancia e fator por distancia percorrida. 
    O fator da distancia varia de acordo com o tipo de pedido.
    O fator_distancia do TipoPedido deve ser multiplicado pela distancia 
    e acrescido ao valor total dos itens. 
    Por exemplo, se o fator_distancia for 2 e a distancia for 5, 
    o total do pedido deve ser acrescido em 10. 
    Ainda, se o cliente for ClienteFidelidade, deve  diminuir o valor total 
    pelo percentual de desconto armazenado no atributo desconto do ClienteFidelidade. 
    Por exemplo, se o valor de desconto for 0.2 e o pedido custar 10, o desconto deve ser
    de 2 e o valor final 8.
    @return um float correspondente ao total do pedido
    '''
    def calcula_valor_pedido(self, distancia: float) -> float:
        soma_itens = 0.0
        for item in self.__itens:
            soma_itens += item.preco_unitario

        total_pedido = soma_itens + (self.__tipo.fator_distancia(soma_itens, distancia) * distancia)

        if isinstance(self.__cliente, ClienteFidelidade):
            total_pedido -= total_pedido * self.__cliente.desconto

        return total_pedido