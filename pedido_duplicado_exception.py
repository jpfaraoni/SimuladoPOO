class PedidoDuplicadoException(Exception):
    def __init__(self, numero):
        # Definindo a mensagem de erro com f-string para incluir o número do pedido
        self.mensagem = f"Pedido {numero} já existe"
        # Chamando o inicializador da classe Exception para passar a mensagem
        super().__init__(self.mensagem)
