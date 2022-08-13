# # Ex. 6
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# #
# buget = int(input('da-mi un buget'))
# print(pret_masini.items())
# print(pret_masini.values())
# for pret in pret_masini.values():
#     print(pret)
#     if pret <= buget:
#         print(f'Pentru un buget de sub {buget} euro puteti alege masina {pret}')

# for masina, pret in pret_masini.items():
#     print(masina + str(pret))
#     if pret <= buget:
#         print(f'Pentru un buget de sub {buget} euro puteti alege masina {masina} cu pretul de {pret} euro')


# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for masina in masini:
# #     print(masina)
# print(masini[0])
# for i in range(len(masini)):
#     # print(i)
#     print(masini[i])
#
# # Ex. 7
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# aparitii = 0
# for numar in numere:
#     if numar == 3:
#         aparitii = aparitii + 1
# print(aparitii)
#
# print(numere.count(3))

# # Ex. 15
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# # tasta ia valorile pe rand [1, 2, 3], [4, 5, 6], [7, 8, 9], [0]
# for tasta in tastatura_telefon:
#     for numar in tasta:
#         print(f'Cifra curenta este {numar}')
#
# for i in range(len(tastatura_telefon)):
#     print(tastatura_telefon[i])
#     for j in range(len(tastatura_telefon[i])):
#         print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# Ex. 14
# numar = int(input('vreau un numar pt piramida'))
# for i in range(1, numar + 1):
#     print(str(i)*i)

# continue - nu mai executa urmatoarele linii de cod din for, merge direct la urmatoarea iteratie - la urmatorul element din lista sau la urmatoarea valoare din range
# break - nu mai executa urmatoarele linii de cod din for, iese de tot din el, nu mai este nicio iteratie, trece la urmatoarea linie de dupa for


'''
WHILE, WHILE ELSE
'''


# cat timp conditia e adevarata, executa urmatorul cod

# de unde incepe, initializam i-ul - adica ca incepe de la zero
# i = 0
# while i <= 3:
# atata timp i <= 3, itereaza
#     print(i)
# ca sa incrementam - adica ca sa treaca la urmatoarea valoare dupa 0, adaugam i + 1, altfel ar printa i = 0 la nesfarsit
#     i = i + 1
#
# declarati variabila de unde incepe
# sa fiti atenti ca si conditia de la while sa devina falsa
#
# i = 1
# prod = 1
# while i <= 20:
#     print(i)
#     prod = prod * i
#     i += 2
# print(prod)
#
# lista = ['alb', 'rosu', 'verde', 'roz']
#
# i = 0
# while i <= len(lista) - 1: # punem -1 pt ca sunt 4 elemente, insa la noi incepe numaratoarea de la 0
# # ori while i < len(lista)
#     print(lista[i])
#     i = i + 1
# # sa afiam din 2 in 2 facem i = i + 2
# else:  # nu e obligatoriu sa punem else ca sa se printeze gata while
#     print('gata while')


'''
FUNCTII sau metode
'''

# un fel de program files unde sunt instalate programele
def print_hi(): # alegem numele metodei/functiei cat mai clar
    '''vom printa cuvantul Hi'''
    print('Hi! Ce faci?')

# un fel de desktop unde avem shortcut catre ele
print_hi()
print_hi()
print_hi()
print_hi()


def creare_triunghi():
    numar = int(input('vreau un numar pt piramida'))
    for i in range(1, numar + 1):
            print(str(i)*i)

# creare_triunghi()
# creare_triunghi()
# creare_triunghi()

# pot sa aiba parametru - sa nu mai citim de la tastatura, sa o rulam de mai multe ori pt orice valoare vrem noi
# parametrii pot sa fie de orice tip: boolean, int, float, string


def creare_triunghi2(numar):
    for i in range(1, numar + 1):
            print(str(i)*i)

creare_triunghi2(2)
creare_triunghi2(7)
creare_triunghi2(9)
creare_triunghi2(1)


def print_hi2(nume, prenume, varsta): # ce avem in paranteza, sunt parametri
    '''vom printa Hi, ce faci'''
    print('Hi!')
    print(f'Ce faci {nume} {prenume}. Ai {varsta} ani?')


print_hi2('Ion', 'Vasile', 67)


# ca sa evitam eroarea in care nu ii dam acelasi nr de parametri de am setat in functie
# putem sa declaram in functie cat e varsta exacta

def print_hi2(nume, prenume, varsta = 85): # ce avem in paranteza, sunt parametri
    '''vom printa Hi, ce faci'''
    print('Hi!')
    print(f'Ce faci {nume} {prenume}. Ai {varsta} ani?')


print_hi2('Ion', 'Vasile')
# dar putem sa si suprascriem varsta declarata in functie
print_hi2('Ion', 'Vasile', 67)

# parametrii sunt de fapt niste variabile declarate dar neinitializate
# vor fi initializate in momentul in care apelam functia respectiva


def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

# la return trebuie sa avem neaparat print ca sa ne dea ceva in consola
# folosim return cand ne intrebam ceva: este par, suma, produs, etc.

print(este_par(34))
print(este_par(51))


def suma(a,b):
    return a+b+b


print(suma(4, 5))


suma2 = suma(3, 4)
print(suma2)
print(suma(suma2, 4))


def nume():
    return 'Ion'


print(nume().upper())