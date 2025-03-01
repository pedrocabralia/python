class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print("Saque efetuado com sucesso")
            
    def mostrarSaldo(self):
        print(f"Saldo: R${self.saldo}")
        
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso")
        