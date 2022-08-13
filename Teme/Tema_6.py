# Ex. 1
class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are raza de {self.raza} si culoarea {self.culoare}')

    def arie(self):
        PI = 3.14
        return f'Aria cercului este de {PI*self.raza**2}'

    def diametru(self):
        return f'Diametrul cercului este de {self.raza*2}'

    def circumferinta(self):
        PI = 3.14
        return f'Circumferinta cercului este de {self.raza*2*PI}'


cerc1 = Cerc (78, 'albastru')
cerc2 = Cerc (59, 'rosu')

cerc1.descrie_cerc()
cerc2.descrie_cerc()

print(cerc1.arie())
print(cerc2.arie())

print(cerc1.diametru())
print(cerc2.diametru())

print(cerc1.circumferinta())
print(cerc2.circumferinta())

print('\n')

# Ex. 2
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def decrie(self):
        print(f'Dreptunghiul are lungimea de '
              f'{self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')

    def arie(self):
        return f'Dreptunghiul are aria de {self.lungime * self.latime}'

    def perimetru(self):
        return f'Dreptunghiul are perimetrul de {2 * (self.lungime + self.latime)}'

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        print()

dreptunghi1 = Dreptunghi(500, 20, 'negru')
dreptunghi2 = Dreptunghi(43, 22, 'alb')

dreptunghi1.decrie()
dreptunghi2.decrie()

print(dreptunghi1.arie())
print(dreptunghi2.arie())

print(dreptunghi1.perimetru())
print(dreptunghi2.perimetru())

dreptunghi1.schimba_culoarea('portocaliu')
dreptunghi1.decrie()
dreptunghi2.schimba_culoarea('verde')
dreptunghi2.decrie()

print('\n')

# Ex. 3
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Ma numesc {self.nume} '
              f'{self.prenume} si am un salariu de {self.salariu} euro.')

    def nume_complet(self):
        return (f'Ma numesc {self.nume} {self.prenume}')

    def salariu_lunar(self):
        return (f'Am un salariu lunar de {self.salariu} euro.')

    def salariu_anual(self):
        return (f'Am un salariu anual de {self.salariu * 12} euro.')

    def marire_salariu(self):
        return (f'Salariul meu a fost marit cu 5%, adica cu {self.salariu * 5/100} euro.')


angajat1 = Angajat('Popescu', 'Ionel', 3000)
angajat2 = Angajat('Florescu', 'Mirela', 5000)

angajat1.descrie()
angajat2.descrie()

print(angajat1.nume_complet())
print(angajat2.nume_complet())

print(angajat1.salariu_lunar())
print(angajat2.salariu_lunar())

print(angajat1.salariu_anual())
print(angajat2.salariu_anual())

print(angajat1.marire_salariu())
print(angajat2.marire_salariu())

print('\n')


# Ex. 4
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} '
              f'are in contul {self.iban} suma de {self.sold} lei.')

    def debibare_cont(self):
        credit_minus = 200
        rest = self.sold - credit_minus
        return f'Am extras suma de {credit_minus} ' \
               f'de lei si am ramas cu un total de {rest} de lei'

    def creditare_cont(self, rest):
        self.sold = rest
        credit_extra = 500
        sum = self.sold + credit_extra
        return f'Am adaugat suma de {credit_extra} ' \
               f'de lei si am un total de {sum} de lei.'


cont1 = Cont('RO66BACX0000001234567890', 'Andrei Ionescu', 15000)
cont2 = Cont('RO66CAC!0000000987654321', 'Petru Badea', 1000)

cont1.afisare_sold()
cont2.afisare_sold()

print(cont1.debibare_cont())
print(cont2.debibare_cont())

print(cont1.creditare_cont(14800))
print(cont2.creditare_cont(800))

print('\n')

# Ex. 5
class Factura:  # not ok
    seria = 'FOC1000001'
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def total(self):
        return self.cantitate * self.pret_buc

    def schimba_cantitatea(self, noua_cantitate):
        self.cantitate = noua_cantitate
        print()


factura1 = Factura(1234, 'Faina', 150, 3)
factura2 = Factura(5678, 'Orez', 100, 5)

from tabulate import tabulate

print(tabulate(factura1, headers=["Numar", "Nume Produs", "Cantitate", "Pret buc"]))
