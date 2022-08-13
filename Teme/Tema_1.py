# Ex. 1
# variabila = zona din memoria unui calculator care tine date; un container, un cosulet

# Ex. 2 + 3
marca_monitor = 'AOC'
print(type(marca_monitor))

model_monitor = 2460
print(type(model_monitor))

pret_monitor = 990.41
print(type(pret_monitor))

full_HD = True
print(type(full_HD))

# Ex. 4
print(round(pret_monitor))
pret_monitor = 990
print(type(pret_monitor))

# Ex. 5
print(f'Mi-am cumparat un monitor marca {marca_monitor}, model {model_monitor}, la pretul de {pret_monitor} lei. Este full HD? {full_HD}')

# Ex. 6
nume = str(input('Numele dvs este: '))
prenume = str(input('Prenumele dvs este: '))
print(f'Numele complet are ' + str(len(nume + prenume)) + ' caractere')

# Ex. 7
lungime = int(input('Lungimea este de: '))
latime = int(input('Latimea este de: '))
print(f'Dreptunghiul cu lungimea de {lungime} si latimea de {latime} are aria de {lungime * latime}')

# Ex. 8
print('Coral is either the stupidest animal or the smartest rock'.count('the'))

# Ex. 9
fraza = 'Coral is either the stupidest animal or the smartest rock'
print(fraza.replace('the', 'THE'))
print('Coral is either the stupidest animal or the smartest rock'.replace('the', 'THE'))

# Ex. 10
x = fraza.isnumeric()
print(x)

# assert fraza.isnumeric()


# Ex. 11
given_string = input('Enter a string: ')

even_chars = []
odd_chars = []

for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
    else:
        odd_chars.append(given_string[i])

print('Odd characters: {}'.format(odd_chars))
print('Even characters: {}'.format(even_chars))

# Ex. 12
def isPalindrome(s):
    return s == s[::-1]


s = 'reper'
ans = isPalindrome(s)
if ans:
    print('Yes')
else:
    print('No')

# Ex. 13
fraza2 = str(input('spune ceva despre tine'))

one, two, three, four, five, *_ = l = fraza2.split()

for n in l:
    print(n)

# sau

fraza3 = 'ma simt bine in seara asta'
one, two, three, four, five, *_ = l = fraza3.split()

for n in l:
    print(n)

# Ex. 14

fraza4 = str(input('ce mai faci?'))
var1 = fraza4[0]
print(fraza4)

# Ex. 15

x, y = input("Enter two values: ").split()
print("nume: ", x)
print("prenume: ", y)
print()
print(x[0].capitalize())

user = input('introdu userul')
parola = input('introdu parola')

print(f'Parola pt user {user} este {parola} si are ' + str(len(parola)) + ' caractere')
