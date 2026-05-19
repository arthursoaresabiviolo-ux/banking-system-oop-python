from abc import ABC, abstractmethod

class Account(ABC): # ABC determines that this is an abstract class
    def __init__(self, number, branch, initial_balance=0.0):
        self._number = number
        self._branch = branch
        self._balance = initial_balance

    @property # transform the method into a property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    @abstractmethod # method that determines that the subclasses will need to have your properly behavior
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def __init__(self, number, branch, initial_balance=0.0, limit=500.0):
        super().__init__(number, branch, initial_balance)
        self.limit = limit

    def withdraw(self, amount):
        available_balance = self._balance + self.limit
        if 0 < amount and amount <= available_balance:
            self._balance -= amount
            return True
        return False

class SavingsAccount(Account):
    def withdraw(self, amount):
        if 0 < amount and amount <= self._balance:
            self._balance -= amount
            return True
        return False

class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account = None

    def link_account(self, account):
        self.account = account

p1 = Client("Arthur", 19)

def menu():
    while True:
        try:
            choice = int(input("""
======================
    Menu Bancário

    1- Criar conta corrente
    2- Criar conta poupança
    3- Depositar
    4- Sacar
    5- Exibir Saldo
    6- Encerrar
======================
Escolha uma das opções: \n"""))
        except ValueError:
            print("\nPor favor, digite um número válido!")
            continue

        if choice < 1 or choice > 6:
            print("\nOpção inválida!")
            
        elif choice == 1 or choice == 2:
            if p1.account is not None:
                print("\nO cliente já possui uma conta ativa!")
            else:
                if choice == 1:
                    p1.link_account(CheckingAccount(number=123, branch="001"))
                    print("\nConta Corrente criada com sucesso!")
                else:
                    p1.link_account(SavingsAccount(number=124, branch="001"))
                    print("\nConta Poupança criada com sucesso!")

        elif choice == 3:
            if p1.account is None:
                print("\nCliente não possui uma conta. Crie uma primeiro!")
            else:
                amount = float(input("\nDigite o valor para depósito: R$ "))
                if p1.account.deposit(amount):
                    print(f"\nDepósito de R$ {amount:.2f} realizado com sucesso!")
                else:
                    print("\nValor de depósito inválido.")

        elif choice == 4:
            if p1.account is None:
                print("\nCliente não possui uma conta. Crie uma primeiro!")
            else:
                amount = float(input("\nDigite o valor para saque: R$ "))
                if p1.account.withdraw(amount):
                    print(f"\nSaque de R$ {amount:.2f} realizado com sucesso!")
                else:
                    print("\nSaldo/Limite insuficiente ou valor inválido.")

        elif choice == 5:
            if p1.account is None:
                print("\nCliente não possui uma conta ativa.")
            else:
                if isinstance(p1.account, CheckingAccount): # check if the object belongs to ContaCorrente class
                    print(f"\nSaldo: R$ {p1.account.balance:.2f} | Limite Especial: R$ {p1.account.limit:.2f}")
                else:
                    print(f"\nSaldo atual: R$ {p1.account.balance:.2f}")

        elif choice == 6:
            print("\nEncerrando o sistema.")
            break

menu()
