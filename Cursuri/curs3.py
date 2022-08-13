# cum citim de la tastatura mai multe variabile
# nume, prenume, varsta = input('vreau un nume, un prenume, varsta').split()
# print(f'numele meu e {nume}, prenumele meu e {prenume} si am {varsta} ani')


text = 'Ioana are zece castraveti si ata'
i = text.count('t')
if i > 3 and i < 5: # if 3 < i < 5
    print(text + 'ttt')
    print(text + 't' * 3)
else:
    print(text.replace('t', ''))


# Tipuri de date: LISTE, TUPLE, SET, DICTIONARE

# LISTA
# pastreaza mai multe valori intr-o sg variabila

lista_masini = ['mazda', 'dacia', 'aro']
lunile_anului = ['ianuarie', 'februarie', 'martie']
lista = ['ana', 'maria', 62626, 56.7, True, False, 'GSGE']
lista_browser = ['chrome', 'firefox', 'safari']

# lista e ordonata - fiecare element are un index, incepe de la 0, daca adaugam un element, il adauga la final
# lista e mutabila - se pot sterge si adauga elemente
# se scrie cu paranteze patrate

print(lista_masini[0])
print(lista[4])

# cum adaugam in lista :
lista_masini.append('renault')  # > cu append - fara sa ii dam pozitia, adauga tot timpul la final
print(lista_masini)
lista_masini.insert(1, 'BMW')  # > ii zicem pozitia pe care sa adauge
print(lista_masini)
lista_masini.insert(4, 5.6)
print(lista_masini)

# insert nu creaza gap-uri, pune direct pe ultima pozitie
lista_masini.insert(90, 'pop')
print(lista_masini)

# asa aflam pe ce pozitie/index e un element
print(lista_masini.index("pop"))

lista_castigatori = ['ion', 'vasile', 'stefan', 0, 6.89]

# cum stergem

# stergem dupa valoare
print(lista_castigatori)
print(lista_castigatori.remove('ion')) # posibil si fara print
print(lista_castigatori)

# asa stergem o anumita pozitie, dupa un numit index
print(lista_castigatori.pop(1))
print(lista_castigatori)

# asa stergem ultimul
print(lista_castigatori.pop())
print(lista_castigatori)

# putem avea valori duplicate
lista = ['ion', 'ion', 'ion', 'dageg', 5, 6, 7, 9, 20, 45, 56]

# lungimea listei
print(len(lista))

# slicing - de unde, pana unde, din cat in cat
print(lista[2:])
print(lista[2::3])

# reverse la lista
print(lista[::-1])
lista.reverse()
print(lista)

# valoarea maxima din lista
print(max(4, 6, 7, 8, 76))

# sortare lista
listaa = [5, 9, 1, 88, 45, 102]
print(listaa)
listaa.sort()
print(listaa)

text1 = 'anamaria'
nume = 'ion'
print(text1[1] + nume[-1])

# in lista putem avea valori duplicate
# se pot schimba valori din lista, suprascriem
lista1 = ['ion', 'ion', 'ion', 'dageg', 5, 6, 7, 9, 20, 45, 56]
lista1[0] = 'vasile'
# lista1[13] = 'gage' > error - out of range
lista1[9] = 'gage'
print(lista1)

# putem avea liste in liste
lista = [3, 4, 'ioana', [3, 5, 5, [1651, 161, 995, 3]], ['ana', 'maria', 'cristina']]
print(lista[1])  #4
print(lista[3][1])  #5
print(lista[3][3]) #afisare lista 3 - [1651, 161, 995, 3]
print(lista[3][3][2])  #995
print(lista[4][2])  #cristina

# extinde lista cu o alta lista
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]
lista = lista2 + lista3
print(lista)

print(lista2)
lista2.extend(lista3)
print(lista2)

lista1 = ['ion', 'ion', 'ion', 'dageg', 5, 6, 7, 9, 20, 45, 56, True, 45.9]
print(type(lista1[0]))
print(type(lista1[4]))
print(type(lista1[-2]))
print(type(lista1[-1]))
print(lista1[0] + lista1[1]) # str cu str
# print(lista1[0] + lista1[4]) # error - no concatenation str with int
print(lista1[0] + str(lista1[4])) # transformam int in str

# SET
# valori unice (nu putem avem duplicate)
# folosim un set cand stim ca valorile nu se pot modifica, adica luni, zodii, etc.
# nu sunt ordonate sau indexate
# sunt imutabile (nu putem schimba locatia elementelor)
# se pot adauga si sterge elemente
# len = lungime
# se scrie cu acolade

culori = {'alb', 'rosu', 'verde'}

print(culori)
# print(culori[0]) > nu putem lua un element de pe o anumite pozitie
culori.add('gri')
print(culori)

# dimensiune
print(len(culori))

# schimbam in lista, adica un fel de type casting
lista = list(culori)
print(lista)
print(lista[0])

# TUPLE
# valorile sunt ordonate si au index
# nu putem adauga sau sterge elemente
# nu accepta duplicate
# len = lungime
fructe = ('mere', 'pere')
print(fructe[0])
print(fructe.index('mere'))
chrome = ('parola', 'username')
yahoo = ('lola@yahoo.com', 'start123')

# dimensiune
print(len(fructe))