class Cliente:
    def __init__(self, endereco, contas):
      self.endereco = endereco
      self.contas = contas

      def realizar_transacao(self, conta, transacao):
         pass

      def adicionar_contas(self, conta):
         pass

class PessoaFisica(Cliente):
  def __init__(self,cpf, nome,data_nascimento):
    super().__init__(self,self.endereco, self.contas)
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento
         
    