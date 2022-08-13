'''
cursul asta o sa fie despre variabile, assert, print, string
'''

# cum printam in consola un mesaj
print('Azi facem cursul 1!')
print(234)

# variabile = un container, un cosulet


# asa declaram si initializam o variabila + valoarea ei

marca_masina = 'Mazda'
model_masina = 'CX-5'
motor = 2200
este_automata = True

print(marca_masina)
print(motor)

# varibilele au nume unic, adica nu putem avea 2 var cu acelasi nume

print(marca_masina)
marca_masina = 'Dacia'
print(marca_masina) # avem suprascriere aici

# variabilele se scriu cu litera mica intotdeauna (constantele se scriu cu litera mare)
# se separa cuvintele cu _

# sunt case sensitive = diferenta intre litera mica sau mare, adica:
Marca_masina = 'Audi'
print(marca_masina) # primul container pt marca
print(Marca_masina) # al doilea container pt marca

# putem sa declaram mai multe variabile deodata (atribuim mai multe valori intr-o sg linie):
numme, prenume, varsta = 'Lazar', 'Giulia', 29
print(varsta)

a = b = c = 6
print(b)

# Tipuri de date

# int - numere intregi (fara numere cu virgula)
varsta = 34
print(varsta)
print(type(varsta)) # metoda ajutatoare ca sa aflam ce tip este o variabila

# float = numere cu virgula
pret = 4.5
print(type(pret))

print(varsta + pret) # putem aduna 2 nr de 2 tipuri de date diferite (int + float)
# print(varsta + marca_masina) >> nu se poate - primim eroare (int+string)

# text de tip string
print(type(marca_masina)) # '' sau ""

# bool / boolean = True / False
is_summer = True
print(type(is_summer))

nume, prenume, varsta = 'Lazar', 'Giulia', 29
# type casting > schimbam tipul variabilei > int => float; int => str, sau din str sa facem float
print(nume + ' ' + prenume + ' are varsta de ' + str(varsta))

# alta varianta decat cea de sus cu str, de fapt cea recomandata:

print(f'Ma numesc {nume} {prenume} si am varsta de {varsta}')
print(f'Am o masina {marca_masina}, modelul {model_masina}, cu motorul {motor}')

pret_masina = 199.999
print(type(pret_masina))
pret_masina = str(pret_masina)
print(type(pret_masina))

# int(), flaot(), str(), bool()

# transformam bool din pret_masina
# cand transformam in bool, o sa ne dea intotdeauna in True
pret_masina = bool(pret_masina)
print(pret_masina)
#
# culoare = 'albastru'
# culoare = int(culoare)
# print(culoare)   # ne da eroare

culoare = '45'
culoare = int(culoare)
print(culoare) # nu ne mai da eroare

# culoare = '45.5'
# culoare = int(culoare)
# print(culoare) # ne da eroare din cauza virgulei

culoare = 45.5
culoare = int(culoare)
print(culoare) # nu ne mai da eroare, il transforma in int => 45

# assert = o verificare ca ceva e adevarat; daca e adevarat, trece mai departe
a = 1
assert a == 1
# assert a == 2 # cum nu e adevarat, o sa primim o eroare

mesaj_de_eroare = 'ai introdus parola gresita'
# deschid pagina
# click pe login
# type username
# type parola
# click login
# intr o variabila salvez mesajul care apare pe pagina
# assert mesaj_de_eroare == 'mesajul salvat de pe pagina' # nu o sa treaca testul de assert si o sa dea eroare
assert mesaj_de_eroare == 'ai introdus parola gresita'

# daca assert urile sunt adevarate, se ruleaza codurile; daca nu, nu mai ruleaza nimic de dupa assert
print('ajungem la linia asta doar daca assertul e true')
# asserturile se fac la final de cod ca sa se ruleze toate codurile

# cum citim de la tastatura = functia input
# cum citim de la tastatura - ne cere sa punem o valoare in consola
ziua = input('astazi este o zi de:')
print(ziua)

# calcul perimetrul unui dreptungi
latime = int(input('latimea este :'))
lungime = int(input('lungimea este: '))
print(f'dreptunghiul cu latime {latime} si lungimea {lungime} are perimetrul {latime + latime + lungime + lungime}')
# ce citim de la tastatura, e string tot timpul
# daca vrem sa fie float sau int, trebuie sa le transformam, adica sa facem type casting

# test automation university - site unde putem face exercitii si cursuri


