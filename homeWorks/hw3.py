class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        ad = input(f'сколько добавите к своим {self._balanse} введите сумму: ')
        print(self._balanse + int(ad))

    def _kill(self):
        if self._balanse > 0:
            print('теперь у вас все наличкой')
            return self._balanse - self._balanse
        else:
            print('у вас не достаточно средств ')
            return self._balanse

    def __jackpot(self):
        self._balanse *= 10

    def get_jeckp(self):
        print(self.__jackpot())


    def _copyy(self, other):
        print(f'ваш сложенный баланс {self._balanse + other._balanse}\n'
              f'было{self._balanse}')




bank = Bank('mbank', 20)
load = Bank('optima', 100)
bank.moneyX()
print(bank._kill())
bank._copyy(load)
print(Bank.get_jeckp(load))
bank.get_jeckp()