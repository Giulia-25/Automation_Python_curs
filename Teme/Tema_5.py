# Ex. 1
def suma(a, b):
    return a+b


print(suma(105, 68))
print(suma(5467, 953138))


# Ex. 2
def par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


print(par(99))
print(par(105988))


# Ex. 3
def nr_total(nume, prenume, nume_mijlociu):
    return len(nume + prenume + nume_mijlociu)


print(nr_total('Giulia', 'Lazar', 'Cristina'))
print(nr_total('Maria', 'Manole', 'Mara'))


# Ex. 4
def arie_dreptunghi(a,b):
    return a*b


print(arie_dreptunghi(9, 8))
print(arie_dreptunghi(15, 36))


# Ex. 5
def arie_cerc(R):
    PI = 3.14
    return PI*R**2


print(arie_cerc(6))
print(arie_cerc(23))


# Ex. 6
def este_litera_m (string):

    if 'm' in string:
        return True
    else:
        return False


print(este_litera_m('mama are mere'))
print(este_litera_m('tata are pere'))


# Ex. 7 - not ok

text = 'fageKJgac'
def number_lower_upper(text):
    lower = 0
    upper = 0
#     for litera in text:
#         if litera.isupper():
#             upper += 1
#         else:
#             if litera.islower():
#                 lower += 1
#     print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')
# number_lower_upper('GEGAGDCF')
# number_lower_upper('gegeaGRGS')
# number_lower_upper('geagag')
# number_lower_upper('Asgeg464')

    for i in range(len(text)):
        if text[i].isupper():
            upper += 1
        else:
            if text[i].islower():
                lower += 1
            print(f'{text} are {lower} atatea caractere mici si {upper} atatea caractere mari')

number_lower_upper('GEGAGDCF')
number_lower_upper('gegeaGRGS')
number_lower_upper('geagag')
number_lower_upper('Asgeg464')


# Ex. 8
def print_lista_numere():
    rezultat = []
    for x in range(1,100):
        if x % 2 == 0:
            rezultat.append(x)
    return rezultat


print(print_lista_numere())


# Ex. 9
def numere(x, y):
    print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    print(f'Numerele sunt egale')
numere(15, 9)

# Ex. 10
# def numere():
#     a = input('da-mi un numar')
#     b, c, d = input('da-mi un set de numere')
#     if a != b and a != c and a != d:
#         return 'am adaugat numarul nou in set'
#     else:
#         return 'nu am adaugat numarul in set. Acesta exista deja'

# print(numere())

# Ex. 11

def an_bisect(an):
    if an % 400 == 0:
        return True
    if an % 100 == 0:
        return False
    if an % 4 == 0:
        return True
    return False

def zi_luna(luna, an):
    if luna in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if luna == 2:
        if an_bisect(an):
            return 29
        return 28
    return 30

print(zi_luna(2, 2022))
print(zi_luna(8, 2022))

# Ex. 12
def calculator(m, n):
    suma = m + n
    scadere = m - n
    inmultire = m * n
    impartire = m / n
    return suma, scadere, inmultire, impartire


print(calculator(10, 2))
print(calculator(100, 25))
