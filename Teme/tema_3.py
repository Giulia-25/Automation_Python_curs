# Ex. 1
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# Ex. 2
print(note_muzicale.count('do'))

# Ex. 3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
print(lista1+lista2) # sau lista = lista1 + lista2 >>> print(lista)
lista1.extend(lista2)
print(lista1)

# Ex. 4
lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

# Ex. 5
# if lista1:
#     print('Lista nu e goala')
# else:
#     print('Lista e goala')

if len(lista1)==0:
    print("lista e goala")
else:
    print("lista nu e goala")

# Ex. 6
lista1.clear()

# Ex. 7
# if lista1:
#     print('Lista nu e goala')
# else:
#     print('Lista e goala')

if len(lista1)==0:
    print("lista e goala")
else:
    print("lista nu e goala")

# Ex. 8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print (dict1.keys())

# Ex. 9
print(f'Ana a luat nota', dict1.get('Ana'))
print(f'Gigel a luat nota', dict1.get('Gigel'))
print(f'Dorel a luat nota', dict1.get('Dorel'))

# Ex. 10
dict1['Dorel'] = 6
print(f'Dorel a facut contestatie si a luat nota', dict1.get('Dorel'))

# Ex. 11
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# Ex. 12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt) # => nu putem avea duplicate

# Ex. 13
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

# Ex. 14
diferente = set(zile_sapt) - set(weekend)
print(diferente)

diferente = set(zile_sapt).symmetric_difference(set(weekend))
print(diferente)

# Ex. 15
intersectie = zile_sapt.intersection(weekend)
print(intersectie)


