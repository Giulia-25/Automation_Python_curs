'''
string, operatori, if
'''

text = 'alabala portocala*'

# fiecare caracter are un index asociat, adica "a" pe indexul 0, "l" pe indexul 1
# numaratoare incepe de la 0
print(len(text))
# len = metoda predefinita care e facuta de cei care au facut programul de Python ca print, sum, etc.
# lungimea textului se afla cu len

# metoddele cu "is" in fata returneaza true sau false si se pot folosi la assert
print(text.isnumeric())
assert text.islower()

# printam fiecare caracter in functie de index
print(text[3])

# print ultimul caracter
print(text[-1])
print(text[17])
# print(text[18])
print(text[len(text) - 1])

# SLICING

# de unde incepem, pana unde (-1) - interval deschis
print(text[3:7])
print(text[0:7])
print(text[:7])  # printeaza de la pozitia 0 pana la 7
print(text[3:])  # printeaza de la pozitia 3 pana la final
print(text[::2])  # printeaza de la inceput la final din 2 in 2
print(text[1::2])  # printeaza de la pozitia 1 pana la final din 2 in 2
print(text[1::5])  # printeaza de la pozitia 1 pana la final din 5 in 5

# print text invers
print(text[::-1])

print(text.capitalize())
print(text.upper())

numar = int(input('vreau un numar'))
print(text[numar])
print(text.replace('bala', 'apa'))

# de unde incepem, pana unde-1, din cat in cat
print(text[1:5:2])

# daca nu pun nimic pe prima pozitie, o considera pozitia 0
print(text[:5:2])
# daca nu pun nimic pe pozitia 2, considera ultima pozitie
# adica o sa afiseze pana la ultima pozitie inclusiv
print(text[::2])
# daca nu pun nimic pe pozitia 3, considera ca merg din 1 in 1, efectiv tot stringul
print(text[::])

# operatori de atribuire, aritmetici, de comparare si logici

# operatori de atribuire: =, +=, -=, *=, /=
maxim = 8
# incrementare
maxim += 1  # si maxim va fi egal cu 9
maxim = maxim + 1
maxim += 10
print(maxim)

maxim -= 5
maxim = maxim - 5
maxim *= 2
maxim = maxim * 2
maxim /= 3
maxim = maxim / 3
print(maxim)
# daca vrem sa ne dea un numar fara virgula, punem 2 slash uri // => Floor division
maxim = maxim // 3
print(maxim)

# operatori ARITMETICI
# +, -, % restul impartirii, // catul, / impartire, * inmultire, ** putere
print(3 ** 2)  # 3 la puterea a doua => 9

# * este valabil si pt texte
print('tatatatatatata')
print('ta' * 7)
numar1 = int(input('vreau un numar'))
numar2 = int(input('vreau al doilea numar'))
print(f'produsul numerelor este {numar1 * numar2}')

# operatori de COMPARARE
# ==, >=, <=, <, >, != (not equal)

assert 5 == 5
assert 5 != 6

# operatori LOGICI

# AND care returneaza true daca amandoua conditiile sunt adevarate
# se foloseste la intervale sau cand 2 conditii trebuie sa fie indeplinite simultan
numar = 9
assert numar >= 2 and numar <= 10
# assert varsta >= 14 and un parinte e cu tine and parintele e proprietar

# OR - sau = minim una din conditii trebuie sa fie adevarata
assert numar >= 2 or numar <= 8

# NOT
assert 5 != 6
# sau:
assert not 5 == 6

# IF = flow control, controlam pe unde merge codul sau ce se intampla = ce se intampla daca

password = 'start123'

user = input('introdu userul')
parola = input('introdu parola')

# ce e in interiorul if-ului se ruleaza doar daca conditia e adevarata
if parola == password:
    print('te-ai logat cu succes')
else:
    print('parola nu e corecta')

if user[0] == 'a':
    print('userul este corect')

numar = 10
numar2 = int(input('vreau un numar'))
if numar2 > numar:
    print(f'{numar2} este maximul')
else:
    print(f'{numar} este maximul')

# daca o conditie e adevarata sau falsa - in fct de asta facem sau executam alte linii de cod

if numar2 > 5 and numar2 < 30:
    print('numarul e in interval')
# sau
if 5 < numar2 < 30:
    print('numarul e in interval')

# Ctrl Alt l = sa pui spatii automat cum trebuie in cod (indentare = indent)

# boundery testing - search

# if (user = = 'cont normal' and parola = 'FFGD') or admin fghj
# if (varsta > 18 and ai pasaport) or (varsta < 18 and (e mama or e tata)) or (etc,)


# ELIF
nota = 7
if nota > 9:
    print('a luat premiul intai')
elif nota > 8:
    print('a luat premiul doi')
else:
    print('a luat locul 3')

suma = 50
if suma >= 40:
    print('ai abonament de 1 giga')
elif suma == 30:
    print('ai abonament de 500 mb')
elif suma == 20:
    print('ai cel mai ieftin abonament')
else:
    print('ai prea putini bani si nu ai net')

luna = input('da-mi un nume de luna')
an = int(input('da mi anul curent'))
if luna == 'decembrie' or luna == 'martie' or luna == 'iunie':
    print('are 30 de zile')
elif luna == 'ianuarie' or luna == 'iulie':
    print('are 31 de zile')
else:
    # verific daca e multiplu de 4 atunci restul impartirii e 0
    if an % 4 == 0:
        print('are 29 de zile')
    else:
        print('are 28 de zile')

# daca avem if si nu avem cod pe partea de true
if not (23 > 10): # 23 nu este mai mic decat 10, pt ca se inverseaza din cauza lui not
    print('egijg')

if not (10 > 23): # 10 este mai mic decat 23, de aceea se citeste printul
    print('gege')

