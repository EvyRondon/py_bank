class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        super().__init__(self, saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques