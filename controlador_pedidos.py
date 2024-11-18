from cliente_fidelidade import ClienteFidelidade
from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    '''
    Busca pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido.
    '''

    def busca_pedido_por_numero(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido

        ...

    '''
    Incluir pedido na lista.
    Tratar os casos de instancias incorretas e pedido duplicado.
    Caso o pedido já exista na lista, gerar a excecao: 
    PedidoDuplicadoException
    '''

    def incluir_pedido(self, pedido):
        try:
            # Verificar se o pedido é None
            if pedido is None:
                return ValueError("Pedido não pode ser None")
            # Verificar se o objeto pedido é realmente uma instância de Pedido
            if not isinstance(pedido, Pedido):
                raise ValueError("O objeto não é uma instância válida de Pedido")
            if pedido.numero in self.__pedidos:
                return PedidoDuplicadoException(pedido.numero)
            #Verificar se o pedido já existe na lista de pedidos
            # for pedido_existente in self.__pedidos:
            #     if pedido_existente.numero == pedido.numero:
            #         raise PedidoDuplicadoException(pedido.numero)  # Levanta exceção de duplicação
        # Se não for duplicado, adiciona o pedido à lista
            self.__pedidos.append(pedido)
            return pedido  # Retorna o pedido incluído

        except ValueError as ve:
            print(f"Erro de valor: {ve}")  # Exibe mensagem de erro em caso de ValueError
        except PedidoDuplicadoException as pde:
            print(f"ERRO: {pde}")  # Exibe a mensagem de erro em caso de pedido

    '''
    Exclui pedido pelo numero.
    Se o pedido nao existir, deve retornar None
    Caso contrario, retorna o pedido excluido
    '''

    def excluir_pedido(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                self.pedidos.remove(pedido)
                return pedido
        return None

    '''
    Deve calcular o total do faturamento para todos os
    itens pedidos por um CPF. 
    Recebe como parametro:
    distancia: um float que corresponde a distancia percorrida
    cpf: uma string representando o CPF do Cliente a ser faturado
    '''

    def calcular_faturamento_pedidos(self, distancia: float, cpf: str):
        soma_faturamento = 0.0
        for pedido in self.__pedidos:
            if pedido.cliente.cpf == cpf:
                soma_faturamento += pedido.calcula_valor_pedido(distancia)
        
        return soma_faturamento
