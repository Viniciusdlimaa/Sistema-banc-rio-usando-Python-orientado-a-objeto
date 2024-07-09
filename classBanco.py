class Conta:
    def __init__(self,numero,titular,saldo) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def Deposito(self):
        valor = float(input('Informe o valor do deposito: '))
        self.saldo = self.saldo + valor
        print(f'Saldo atual: {self.saldo}')
    def Saque(self):
        valor = float(input('Informe o valor do saque: '))
        if valor>self.saldo:
            print(f'Saque negado, valor superior ao saldo\nSaldo atual: {self.saldo}')
        else:
            self.saldo = self.saldo + valor
            print(f'Saque efetuado com sucesso!\nSaldo atual: {self.saldo}')
    def Exibir_saldo(self):
        print(f'Seu saldo atual: {self.saldo}')
class Banco:
    def __init__(self,lista_contas=[]) -> None:
        self.lista_contas = []
    def Adicionar_conta(self,conta):
        self.lista_contas.append(conta)
    def Remover_conta(self):
        numero_conta = int(input('Informe o numero da conta: '))
        for i,item in enumerate(self.lista_contas):
            if item.numero == numero_conta:
                print(f'Numero:{item.numero}\nTitular: {item.titular}\nSaldo: {item.saldo}')
                op = str(input('Tem certeza que deseja remover essa conta? [S/N] ')).upper().strip()[0]
                if 'S' in op:
                    del(self.lista_contas[i])
                    print('Conta removida!')
                else:
                    print('A conta não removida')
            elif i == len(self.lista_contas):
                print('Conta não encontrada')
    def Listar_contas(self):
        txt = 'CONTAS CADASTRADAS NO BANCO'
        print(txt.center(50))
        for i,item in enumerate(self.lista_contas):
            print('--'*30)
            print(f'N°: {item.numero}\nTitular: {item.titular}\nSaldo: {item.saldo}')
    def Buscar_conta(self):
        numero_conta = int(input('Informe o numero da conta: '))
        for i,item in enumerate(self.lista_contas):
            if item.numero == numero_conta:
                print(f'Numero:{item.numero}\nTitular: {item.titular}\nSaldo: {item.saldo}')
            elif i == len(self.lista_contas):
                print('Conta não encontrada')
conta1 = Conta(numero=123654,titular='Vinicius Lima',saldo=0)
conta2 = Conta(numero=789654,titular='Julia Barros',saldo=0)
conta3 = Conta(numero=456123,titular='Philipe Henrrique',saldo=0)
conta4 = Conta(numero=321456,titular='Eva Pereira',saldo=0)
conta1.Deposito()
conta4.Deposito()
conta3.Deposito()
conta1.Saque()
brb = Banco()
brb.Adicionar_conta(conta=conta1)
brb.Adicionar_conta(conta=conta2)
brb.Adicionar_conta(conta=conta3)
brb.Adicionar_conta(conta=conta4)
brb.Listar_contas()
brb.Buscar_conta()
brb.Remover_conta()