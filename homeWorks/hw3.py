class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        ad = input(f'сколько добавите к своим {self._balance}, введите сумму: ')
        print('Новый баланс: ', self._balance + int(ad))

    def _kill(self):
        if self._balance > 0:
            print('теперь у вас все наличкой')
            return f'ваш баланс обнулен: {self._balance - self._balance}'
        else:
            print('у вас не достаточно средств ')
            return self._balance

    def __jackpot(self):
        self._balance *= 10

    def get_jeckpot(self):
        print(self.__jackpot())


    def _copyy(self, other):
        print(f'ваш сложенный баланс {self._balance + other._balance}\n'
              f'было {self._balance}')

class Bank2(Bank):

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance


    name = property(get_name, set_name)
    balance = property(get_balance, set_balance)


class Bank3(Bank):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print('Недопустимый баланс')
        else:
            self._balance = balance

bank1 = Bank('Jaka', 500)
bank2 = Bank2('Alina', 1000)
bank3 = Bank3('Arina', 2000)

bank1.moneyX()
print(bank1._kill())
bank1.get_jeckpot()
bank1._copyy(bank2)

bank2.name = 'Alim'
print(bank2.name)
bank2.balance = 1500
print(bank2.balance)

bank3.name = 'Vova'
print(bank3.name)
bank3.balance = -500
print(bank3.balance)












