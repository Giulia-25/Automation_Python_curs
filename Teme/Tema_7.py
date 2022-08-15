from abc import ABC, abstractmethod


class FormaGeometrica (ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')



class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria este de {self.__latura**2}')



class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None

    def aria(self):
        print(f'Aria este de {FormaGeometrica.PI*self.__raza**2}')

    def descrie(self):
        print('Eu nu am colturi')


patrat1 = Patrat(3)
patrat1.descrie()
patrat1.aria()

print('\n')


patrat1.latura = 6
patrat1.latura
del patrat1.latura
patrat1.latura

print('\n')

cerc1 = Cerc(6)
cerc1.descrie()
cerc1.aria()

print('\n')

cerc1.raza = 15
cerc1.raza
del cerc1.raza
cerc1.raza