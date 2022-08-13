from Cursuri.curs6 import Elev

elev1 = Elev('Muresan', 'Ioana', 45958)
print(elev1.nume)

'''Ex. 7

string2 = 'Mama se uita pe Netflix la HERO'

def nr_caractere(string2):
        my_counter=0
        for i in string2:
         if i.islower():
            my_counter=my_counter+1

print(nr_caractere('Mama se uita pe Netflix la HERO'))


def upperlower(string):
    upper = 0
    lower = 0

    for i in range(len(string)):

        # For lower letters
        if (ord(string[i]) >= 97 and
                ord(string[i]) <= 122):
            lower += 1

        # For upper letters
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            upper += 1

    print('Lower case characters = %s' % lower,
          'Upper case characters = %s' % upper)


# Driver Code
string = 'GeeksforGeeks is a portal for Geeks'
upperlower(string)


def nr_caractere(string2):
    x = 0
    for litera in string2:
        if litera.islower():
            x = x + 1
    return x

print(nr_caractere('Mama se uita pe Netflix la HERO'))'''

# def numere():
#     a = input('da-mi un numar')
#     b, c, d = input('da-mi un set de numere')
#     if a != b and a != c and a != d:
#         return 'am adaugat numarul nou in set'
#     else:
#         return 'nu am adaugat numarul in set. Acesta exista deja'

# print(numere())


# class Bank_Account:
#     def __init__(self, iban, titular_cont, sold):
#         # self.balance = 0
#         # print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def deposit(self):
#         amount = float(input("Enter amount to be Deposited: "))
#         self.sold += amount
#         print("\n Amount Deposited:", amount)
#
#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.sold >= amount:
#             self.sold -= amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
#
#     def display(self):
#         print("\n Net Available Balance=", self.sold)
#
# s = Bank_Account('RO66BACX0000001234567890', 'Andrei Ionescu', 15000)
#
# s.deposit()

from tabulate import tabulate

d = [ ["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

print(tabulate(d, headers=["Name", "Age", "Percent"]))