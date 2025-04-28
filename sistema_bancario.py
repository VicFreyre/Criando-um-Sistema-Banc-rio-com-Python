class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios < 3:
            if valor <= 500.0 and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_diarios += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            elif valor > 500.0:
                print("O limite de saque por vez é de R$ 500,00.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Você atingiu o limite de 3 saques diários.")

    def extrato(self):
        print("\nExtrato Bancário:")
        if self.depositos:
            print("Depósitos:")
            for deposito in self.depositos:
                print(f"R$ {deposito:.2f}")
        else:
            print("Nenhum depósito realizado.")
        
        if self.saques:
            print("Saques:")
            for saque in self.saques:
                print(f"R$ {saque:.2f}")
        else:
            print("Nenhum saque realizado.")
        
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
    
conta = ContaBancaria()

conta.depositar(1000.50)
conta.depositar(500.00)

conta.sacar(200.00)
conta.sacar(450.00)
conta.sacar(100.00)

conta.extrato()
