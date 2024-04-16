class contaBancaria:
    
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Numero da conta:", self.numero)
        print("Titular", self.titular)
        print("Saldo:", self.saldo)


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("O seu saldo inuficiente")
        
def exibir_menu():
    print("\nmenu")
    print("1 - Exibir detalhes da conta")
    print("2 - Realizar depositos")
    print("3 - Realizar saque")
    print("0 - Sair do programa")   

numero_conta = input("Digite o numero da conta:")
titular_conta = input("Digite o titular da conta:")
saldo_inicial = float(input("Digite o saldo inicial da conta:"))

conta_do_usuario = contaBancaria(numero_conta, titular_conta , saldo_inicial)

opcao = None 

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite a opcao desejada:"))
    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("digite o valor que sera depositado:").replace(",","."))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("digite o valor que sera sacado:"))
        conta_do_usuario.sacar(valor_saque)
    elif opcao == 0:
        print("0 - Sair")


conta_do_usuario.exibir_detalhes()
