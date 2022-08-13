# testare manuala
# regression, chain smoke, white box testing, black box testing
# cum se face un test case, cum se raporteaza un bug, severity, priority
# testare functionala, non-functionala, performanc
# tools = jira
# agile, waterfall

# schimbari_maxime = 3
# jucatori = ['J1', 'J2', 'J3', 'J4', 'J5']
# schimbari_efectuate = 2
# jucator_in = 'J6'
# jucator_out = "J2"
#
# if jucator_out in jucatori and schimbari_efectuate < 3:
#     print('se va efectua schimbarea')
#     # ori pot sa sterg J4 folosing metoda remove in care trebuie sa ii dau ca si parametru valoarea
#     # stergere folosing pozitia
#     # print(jucatori.index(jucator_out))
#     # jucatori.pop(jucatori.index(jucator_out))
#     print(jucatori)
#     jucatori.remove(jucator_out)
#     print(jucatori)
#     jucatori.append(jucator_in)
#     print(jucatori)
#     schimbari_efectuate += 1
#     print(f'A iesit jucatorul {jucator_out}, a intrat jucatorul {jucator_in}, mai aveti {schimbari_maxime-schimbari_efectuate} schimbari')
# else:
#     if jucator_out in jucatori:
#         print('nu mai aveti schimbari')
#         print(f'mai aveti {schimbari_maxime - schimbari_efectuate}')
#     else:
#         print(f'nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
#
#
# lista = ['ioana', 'maria', 'cristina']
# lista.remove('cristina')
# print(lista)
#
# lista2 = ['ioana', 'maria', 'vasile']
# lista2.pop(0)
# print(lista2)
#
# index = lista2.index('vasile')
# print(f'vasile e pe pozitia {index}')
# lista2.pop(index)
# print(lista2)

# DICTIONARE (key-value)
# sunt ordonate
# sunt mutabile, valorile pot fi schimbate
# cheile sunt unice, nu putem avea chei duplicate (chei = porecle pt index uri)


parole = {'Chrome':'gege', 'Firefox':'gegea', 'Yahoo':'gege', 'Google':'gegaaae'}
pin = {'mastercard':1234, 'visa': 7846, 'revolut':99998}
lista_produse = ['aspirator', 'laptop', 'aragaz']
lista_preturi = [4.55, 67.8, 78.9, 456]
dict_produse = {'aspirator': 4.56, 'laptop': 56.7, 'aragaz': 789} # dict exista ca sa evitam sa facem liste

# # asa aflam lungimea
# print(len(dict_produse))
# #
# # #asa aflam valoarea unei key-chei
# # print(dict_produse['aspirator'])
# # print(dict_produse.get('aspirator'))
# #
# # adaugam elemente, facem update-suprascriere/modificare
# dict_produse['frigider'] = 89.0
# print(dict_produse)
# # folosim metoda asta cand vrem sa adaugam mai multe valori
# dict_produse.update({'masa': 678, 'banca': 980})
# print(dict_produse)
# #
# # key-cheia este unica => suprascrierea valorii unei key
# dict_produse['aspirator'] = 909
# print(dict_produse)
#
# # asa stergem - trebuie sa specificam cheia
# dict_produse.pop('banca')
# print(dict_produse)
#
# # printare doar key
# print(dict_produse.keys())
# # printare doar valori
# print(dict_produse.values())
# # printare cu totul
# print(dict_produse.items())
#
# if 'masa' in dict_produse.keys():
#     print('este valoarea')
#
# lista_vocale = ['a', 'e', 'i']
# if 'a' in lista_vocale:
#     print('e vocala')
#
produs = 'aspirator'
# if produs in dict_produse.keys():
#     print('produsul e in lista de chei')
#     print(dict_produse[produs])
#     print(f'{produs} are pretul {dict_produse[produs]}')
#     print(f'{produs} are pretul {dict_produse.get(produs)}')
# else:
#     print('produsul nu e in lista')
#
# pret = 9.99
# if produs in dict_produse.values():
#     print('produsul e in lista de valori')
# else:
#     print('produsul nu e in lista de valori')


# FOR
# structuri repetitive, se repeta de mai multe ori atata timp cat este adevarat
# pentru conditia de unde incepe i = 0, unde se termina si din cat in cat sa mearga

# range e un interval: de unde incepe, unde se termina si din in cat merge

# x e intre -3, 20 => 3 variante de scriere:
# x > -3 and x < 20
# -3 < x < 20
# x in range (-3, 20)
# x in range(30) = echivalent cu x in range (0, 30)
# se poate adauga si x in range (0, 30, 2) - sa mearga din 2 in 2
# cand ne referim la numere folosim: i, j, k


for i in range(0,4): # sau for i in range(4) => 0 e optional
    print(i)
    print('ana are mere') # pt fiecare valoare printeaza si asta

sum = 0
for i in range(4): # aici incepe de la 0 pana la 3
    sum = sum + i # sau sum += i
print(sum)

sum = 0
for i in range(230): # aici incepe de la 0 pana la 229
    sum = sum + i # sau sum += i
    # print(sum) # ca sa aflam care e suma intermediara
print(sum)

prod = 1
for i in range(1, 9):
    prod = prod * i
print(prod)

prod = 1
for i in range(1, 230, 10):
    prod = prod * i
else: # nu e obligatoriu sa punem else
    print('am terminat')
print(prod)

# asa parcurgem o lista cand avem nevoie de indexurile ei
masini = ['mercedes', 'volvo', 'dacia', 'trabant', 'aro']
print(masini)
for i in range(len(masini)):
    print(masini[i]) # i este indexul si o sa aiba valoarea 0 = mercedes, 1 = volvo, etc.


masini = ['mercedes', 'volvo', 'dacia', 'trabant', 'aro']
# print(masini)
len = len(masini)
for i in range(len):
    print(masini[i])
    if masini[i] == 'volvo':
        masini[i] = 'cielo'
    if masini[i].islower():  # ai nevoie de index ca sa poti face modificari din astea
        masini[i] = masini[i].upper()
print(masini)

# FOR EACH
# for masina in masini:
#     print(masina)
#
# culori = ['alb', 'verde', 'roz']
# for culoare in culori:
#     print(culoare)
#     # if culoare == 'verde':
#     #     culori.remove(culoare)
#     if culoare == 'roz':
#         culori.append(culoare) # continua sa mearga in loop
# print(culori)

# parole = {'Chrome':'gege', 'Firefox':'gegea', 'Yahoo':'gege', 'Google':'gegaaae'}
# for key, value in parole.items():
#     # print(key)
#     # print(value)
#     print(f'siteul {key} are parola {value}')

vocale = ['a', 'e', 'i']
for vocala in vocale:
    print(vocala)

# BREAK = daca vreau sa sar peste un pas; iese din cod

masini = ['mercedes', 'volvo', 'dacia', 'trabant', 'aro']

# for masina in masini:
#     print(masina)
#     if masina == 'volvo':
#         print('cea mai tare din parcare')
#         break # dupa acest break iese din for si se duce la urmatorul prim tab

# CONTINUE - sare peste pasi si merge la urmatoarea iteratie

for masina in masini:
    # print(masina)
    if masina == 'volvo':
        print('cea mai tare din parcare')
        continue
    print(masina+masina)