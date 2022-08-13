def sum(a,b):
    return a + b


def sum2(a, b):
    print(a + b)


print(sum(3, 4))
suma = sum(3, 4) # salvam intr o variabila
print(sum(suma, 5))
sum2(10, 10)
print(sum2(10, 10)) # gresit, ne da None pt ca avem deja un print si nu un return


text = 'ana'
print(text.islower())

'''
OOP - part 2
'''

# 4 piloni ai OOP:

'''
Inheritance (mostenire):
'''

# 2 clase: o clasa o sa ia denumirea de parinte si o clasa ia denumirea de copil
# clasa copil o sa mosteneasca toate atributele si metodele din clasa parinte
# clasa parinte poate sa aiba oricati copii


# clasa parinte
class Chef:
    def make_salad(self):
        print('make salad')

    def make_eggs(self):
        print('make eggs')

    def make_fries(self):
        print('make fries')


# clasa copil
class Chef_Italian(Chef): # scriem intre paranteze pe cine mosteneste

    def make_pasta(self):
        print('make pasta')

    def make_pizza(self):
        print('make pizza')


class Chef_Japanese(Chef):

    def make_sushi(self):
        print('make sushi')

    def make_rice(self):
        print('make rice')


Mariuca = Chef()
Mariuca.make_eggs()

Antonio = Chef_Italian()
Antonio.make_salad()
Antonio.make_pizza()

Yung = Chef_Japanese() # el nu va sti sa gateasca ce stie Chef Italian
Yung.make_salad()
Yung.make_sushi()


'''
Polymorphism
'''

# functii cu acelasi nume dar cu un comportament diferit


def sum(a, b, c = 0):
    return a + b + c


print(sum(3, 4, 5))
print(sum(3, 4))


# Polymorphism with inheritance


class Bird:
    def describe(self):
        print('I am a bird.')

    def fly(self):
        print('I can fly!')

    def sing(self):
        print('I cip cip cirip!')


class Randunica(Bird):
    def fac_cuib(self):
        print('Adun iarba')


class Pinguin(Bird):
    def fly(self):
        print('Nu sunt chiar asa bun la zbor')


class Papagal(Bird):
    def sing(self):
        print('Eu nu fac cip cip cirip, eu vorbesc.')


Coco = Papagal()
Coco.sing()


Pingu = Pinguin()
Pingu.describe()
# daca avem 2 functii cu acelasi nume, se foloseste functia din clasa copil
Pingu.fly()


'''
Encapsulation
'''

# cand ascundem atributele si folosim getter sau setter sa ajungem la ele
# si metodele pot fi ascunse
# se ascund daca punem __


class Car:
    __color = 'grey' # am ascuns atributul color

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def describe(self):
        print(f'Vrum Vrum! My car is {self.__color}')
        # print(self.__color)

    def __hidden(self):
        print('nu o poti vedea oricum')

    # def __init__(self, cutie):
    #     self.__cutie = cutie # nu va putea fi printata sau modificata fara getter sau setter


Dacia = Car()
print(Dacia.get_color())
Dacia.describe()

# Dacia.culoare = 'green' # nu mai merge sa suprascriem asa
Dacia.set_color('green')
print(Dacia.get_color())
Dacia.describe()


'''
Abstraction
'''

# o clasa abstracta e o clasa fara corp (nu sunt definite metodele)
# are doar metode cu logica definita, adica numele metodei
# o interfata e o clasa care contine doar metode abstracte
# metodele abstracte sunt metode ce trebuie implementate neaparat de toti mostenitorii


# avem nevoie de acest import pt abstractizare in Python

from abc import ABC, abstractmethod


# clasa abstracta poate sa contina metode abstracte
# clasa interfata contine doar metode abstracte


class Bird(ABC):
    def describe(self):
        print('I am a bird.')

    # se foloseste acest decorator ca sa evidentiem ca e o metoda abstracta
    # metoda abstracta = metoda fara corp (fara logica interna)
    @abstractmethod
    def fly(self):
       pass

    def sing(self):
        print('I cip cip cirip!')


class Parrot(Bird):
    def varsta(self):
        print('Am 4 ani')

    def fly(self):
        print('I can fly!')


Coco = Parrot()
Coco.describe()


# clasa interfata (Interface) = toate metodele sunt abstracte
# obliga clasele mostenitoare sa implementeze toate functiile - ca si cum ar fi functii required
class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def pedigree(self):
        raise NotImplementedError

    @abstractmethod
    def home(self):
        raise NotImplementedError

# clasa care mosteneste clasa interfata de mai sus

class Dog(Animal):

    def nume(self, nume):
        print(f'Numele meu este {nume}')

    def sound(self):
        print('Ham ham!')

    def pedigree(self):
        return True

    def home(self):
        print('doarme in pat')


Rex = Dog()
Rex.nume('Rex')

# vom primi eroarea: Can't instantiate abstract class Dog with abstract methods home, pedigree, sound
# pt ca nu am definit sound, pedigree si home


'''
Exceptii
'''

# sunt erori, ceva ce nu poate sa faca codul si il opreste din executie

# lista = [1, 2, 3, 4, 5]
# print(lista[6]) # primim eroarea => IndexError: list index out of range

# in try punem codul periculos
try:
    lista = [1, 2, 3, 4, 5]
    print(lista[6])
# punem numele erorii ce ne apare
except IndexError as e: # 'e' poate fi orice litera sau error sau orice
    print('Ai o pozitie mai mare decat lungimea listei')

numar_elevi = int(input('da-mi un numar'))
if numar_elevi > 30:
    raise IndexError('Limita elevilor e de 30')


