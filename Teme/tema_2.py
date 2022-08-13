# Ex. 1
# if else = daca o conditie este adevarata, se executa if si daca nu, se executa else

# Ex. 2
x = int(input('Da-mi un numar x'))

if x > 0:
    print(f'{x} este numar natural')
elif x < 0:
    print(f'{x} nu este numar natural')
elif x == 0:
    print(f'{x} nu este numar natural')

# Ex. 3
if x > 0:
    print(f'{x} este numar pozitiv')
elif x < 0:
    print(f'{x} este numar negativ')
elif x == 0:
    print(f'{x} este numar neutru')


# Ex. 4
if -2 < x < 13:
    print('numarul este in interval')
else:
    print('numarul nu este in interval')

# Ex. 5
y = int(input('Da-mi un numar y'))
if x - y < 5:
    print('numarul este in interval')
else:
    print('numarul nu este in interval')

# Ex. 6
if not 5 < x < 27:
    print('numarul nu este in interval')
else:
    print('numarul este in interval')

# Ex. 7
if x == y:
    print('cele doua numere sunt egale')
elif x > y:
    print('primul numar este mai mare ca al doilea')
elif x < y:
    print('al doilea numar este mai mare ca primul')

# Ex. 8
z = int(input('Da-mi un numar z'))
if x + y == x + z:
    print('Triunghiul este isoscel')
elif z + y == x + z == y + z:
    print('Triunghiul este echilateral')
else:
    print('Triunghiul este oarecare')
# nu sunt sigura daca proprietatile sunt ok - m-a batut geometria dintotdeauna :)))

# Ex. 9
litera1 = str(input('Da-mi o litera'))
if litera1 == 'a' or litera1 == 'e' or litera1 == 'i' or litera1 == 'o' or litera1 == 'u':
    print(f'Litera ' + str(litera1) + ' este o vocala')
else:
    print(f'Litera ' + str(litera1) + ' este o consoana')

# Ex. 10
nota1 = int(input('Ce nota ai luat?'))
if nota1 >= 9:
    print('Felicitari, ai luat A!')
elif nota1 >= 8:
    print('Felicitari, ai luat B!')
elif nota1 >= 7:
    print('Este loc de imbunatatire, ai luat C!')
elif nota1 >= 6:
    print('Este loc de imbunatatire, ai luat D!')
elif nota1 >= 4:
    print('Este loc de imbunatatire, ai luat E!')
elif nota1 <=4:
    print('Trebuie sa vorbim, ai luat F!')

# Ex. 11
if x > 1000:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

# Ex. 12
if len(str(x)) == 6:
    print(f'{x} are exact 6 cifre')
else:
    print(f'{x} nu are fix 6 cifre')

# Ex. 13
x1 = int(input('Alege un numar'))
if (x1 % 2) == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

# Ex. 14
list1 = [x, y, z]
max_number = max(list1)
print(f'Cel mai mare numar este ' + str(max_number))

# sau
max_number = max(x, y, z)
print(f'Cel mai mare numar este {max_number}')

# Ex. 16
fraza = 'Coral is either the stupidest animal or the smartest rock'
print(fraza[0:-x])

# Ex. 17
fraza1 = fraza[0:5] + fraza[-5:]
print(fraza1)

# Ex. 18
import re
cuvant = re.search(r'\b(rock)\b', fraza)
print(cuvant.start())
print(fraza[0:53])

# Ex. 19
fraza2 = str.lower(input('Spune-mi ceva despre tine'))
assert fraza2[0] == fraza2[-1]

# Ex. 20
sir = '0123456789'
print(sir[::2])
print(sir[1::2])

# Ex. 21
Varsta = int(input('Ce varsta aveti?'))
Insotit_de_mama = False
Insotit_de_tata = True
Pasaport = False
Act_permisiune_mama = False
Act_permisiune_tata = True

if Varsta >= 18 and Pasaport == True:
    print('Aveti perimisiunea de a va imbarca')
else:
    print('Nu aveti perimisiunea de a va imbarca')

if Varsta < 18 and Pasaport == True and Insotit_de_tata == True and Insotit_de_mama == True:
    print('Aveti perimisiunea de a va imbarca')
else:
    print('Nu aveti perimisiunea de a va imbarca')

if Varsta < 18 and Pasaport == True and Insotit_de_tata == True and Act_permisiune_mama == True:
    print('Aveti perimisiunea de a va imbarca')
else:
    print('Nu aveti perimisiunea de a va imbarca')

if Varsta < 18 and Pasaport == True and Insotit_de_mama == True and Act_permisiune_tata == True:
    print('Aveti perimisiunea de a va imbarca')
else:
    print('Nu aveti perimisiunea de a va imbarca')

# Ex. 22
dice_roll = int(input('Alege un numar'))
import random
print(random.randint(1,6))
if str(dice_roll) > str(random.randint(1,6)):
    print(f'Ai pierdut. Ai ales un numar mai mare.')
elif str(dice_roll) < str(random.randint(1,6)):
    print(f'Ai pierdut. Ai ales un numar mai mic.')
elif str(dice_roll) == str(random.randint(1,6)):
    print(f'Ai ghicit. Felicitari!')
