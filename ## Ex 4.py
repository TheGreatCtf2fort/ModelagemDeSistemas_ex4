## Ex 4 

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Transacao:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def registrar(self, conta):
        if self.tipo == "deposito":
            conta.depositar(self.valor)
        elif self.tipo == "saque":
            conta.sacar(self.valor)

    def adicionar_transacao(self, historico):
        historico.append(self)


class Conta:
    def __init__(self, cliente, numero, agencia="0001", limite=500, limite_saques=3):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = []
        self.limite = limite
        self.limite_saques = limite_saques

    def consultar_saldo(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        elif valor > self.limite:
            print("Valor excede o limite")
        else:
            self.saldo -= valor
            print("Saque realizado")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado")
        else:
            print("Valor inválido")
