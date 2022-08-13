# recap FUNCTII

# FUNCTII SIMPLE - nu au parametrii - adica nu au nimic intre paranteze
# functiile printeaza ceva sau returneaza ceva
# def text():
#     print('fara return')
# text()
#
# # FUNCTII cu return - returneaza un text, etc, orice tip de date; salvam rezultatul intr o variabila
# def text2():
#     return 5
# print(text2())
#
# varsta = text2()
# print(varsta)
#
# def get_aria():
#     return 10
#
# def is_par():
#     return True
#
# def is_Submit_button_displayed():
#     return True
#
# # care returneaza True sau False incep cu is
# # care ne dau un text sau o valoare incep cu get_
#
# def este_par(numar): # numar = parametru
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
#
# def este_par2(numar): # varianta nr.2
#     return numar % 2 == 0
#
# print(este_par(3))
# print(este_par(310))
# print(este_par2(310))

# text = 'gehrhsh'
# def number_lower_upper(text):
#     lower = 0
#     upper = 0
#     for i in range(len(text)):
#         if text[i].isupper():
#             upper += 1
#     else:
#         if text[i].islower():
#             lower += 1
#     print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')
#     if lower == len(text) or upper == len(text):
#         return True
#     else:
#         return False
#
# number_lower_upper('Ad')
# toate_literele_de_un_fel = print(number_lower_upper('Ad'))
# print(toate_literele_de_un_fel)
# toate_literele_de_un_fel = print(number_lower_upper('ADDDDGEG'))
# print(toate_literele_de_un_fel)
#
# def log_in():
#     print(f'Ma loghez cu user Giulia si parola 123')
#
# log_in()
#
#
# def login(user, parola):
#     print(f'ma loghez cu user {user} parola {parola}')
#
#
# login('ioana', '123')
# login('vasile', 'fawgeeg')
# login('admin', '154GEGSDF')
#
#
# def login1(user, parola = '123'):
#     print(f'ma loghez cu user {user} parola {parola}')
#
#
# login1('admin')
# login1('admin', 'gegavgd') # suprascriere
#
#
# def perimetru(latime, lungime):
#     # perimetru = 2*latime+2*lungime
#     # return perimetru
#     return 2*latime+2*lungime


'''
OOP - programare orientata pe obiect
'''

class Car:
# clasa este o reteta (blueprint) pt crearea obiectelor
# "Car" este obiectul - instanta clasei

# fields / atribute / variabile
    marca = 'Dacia'
    model = '1100'
    year = 2000
    color = 'black'

# metode (methods)
    def accelerate(self):
        print('Vrum, vruuum')
    def descrie(self):
        print(f'am masina super tare {self.marca}, {self.model} din anul {self.year}')
    def stop(self):
        print('Stop!')

# folosim SELF ca sa le putem apela - ajuta functia sa aiba acces la atributele/metodele clasei

ioana = Car()

print(ioana.color)
ioana.color = 'verde'
print(ioana.color)

ioana.descrie()
ioana.marca = 'BMW'
print(ioana.descrie()) # sau ioana.descrie()
ioana.marca = 'Dacia' # nu putem sa dam reset, trebuie sa suprascriem iar
print(ioana.descrie())

print(ioana.year)
ioana.year = 4562
print(ioana.year)

felicia = Car()
elena = Car()
ioana.stop()
felicia.accelerate()
elena.descrie()


class Elev:
    # fields / atribute

    lista_note = []
    merge_la_curs = False

    # constructor
    # asa folosim parametri la clasa, ca si atribute obligatorii
    def __init__(self, nume, prenume, cod_matricol):
        self.nume = nume
        self.prenume = prenume
        self.cod_matricol = cod_matricol
    # metode
    def descrie(self):
        print(f'Ma cheama {self.nume} {self.prenume} si am cod matricol {self.cod_matricol}')

    def adauga_nota(self, nota):
        self.lista_note.append(nota)

    def media(self):
        sum = 0
        for nota in self.lista_note:
            sum += nota
        return sum/len(self.lista_note)


elev1 = Elev('Muresan', 'Ioana', 45958)
print(elev1.nume)

elev1.descrie()

print(elev1.lista_note)
elev1.adauga_nota(3)
print(elev1.lista_note)
elev1.adauga_nota(8)
print(elev1.lista_note)

print(elev1.media())
elev1.merge_la_curs = True

elev2 = Elev('Vasile', 'Mara', 42064)