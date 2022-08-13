# Ex.1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# a)
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
# b)
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
#
# c)
# i = 0
# while i <= len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i = i + 1

# Ex. 2
# for i in range(1, 8):
#     masini[i] = masini[i].upper()
#     print(masini)

# # Ex. 3
# for masina in masini:
#     # print(masina)
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs')
#         break
#     if masina != 'Mercedes':
#         print(f'Am gasit masina {masina}. Mai cautam.')

# # Ex. 4
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f's-ar putea sa va placa masina {masina}')

# # Ex. 5
# masini_vechi = []
# # print(masini)
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f'Modele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')

# Ex. 6
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
#
# buget = 15000
# for masina, pret in pret_masini.items():
#     # print(masina + str(pret))
#     if pret <= buget:
#         print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina} cu pretul de {pret}')

# Ex. 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere)
# item_3 = 0
#
# for numar in numere:
#     if numar == 3:
#         item_3 += 1
# print(item_3)
#
# # Ex. 8
# print(numere)
# total_suma = 0
# for i in range(len(numere)):
#     total_suma = total_suma + i
# print(total_suma)

# Ex. 9
# print(numere)
# numar_maxim = numere[0]
# for numar in numere:
#     if numar > numar_maxim:
#         numar_maxim = numar
# print(numar_maxim)

# Ex. 10
# print(numere)
# for numar in numere:
#     if numar >= 1:
#         print(f'-{numar}')
#     else:
#         print(f'{numar}')

# Ex. 11
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# print(alte_numere)
# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar >= 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

# Ex. 12
# Bubble sort in Python

# def bubbleSort(array):
#     # loop to access each array element
#     for i in range(len(array)):
#
#         # loop to compare array elements
#         for j in range(0, len(array) - i - 1):
#
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if array[j] > array[j + 1]:
#                 # swapping elements if elements
#                 # are not in the intended order
#                 # temp = 45
#                 # 45 -> 0
#                 # 0 = temp = 45
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#
# data = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# bubbleSort(data)
#
# print('Sorted Array in Ascending Order:')
# print(data)

# Ex. 14
# numar = int(input('vreau un numar'))
# for i in range(1, numar + 1):
#     print(str(i)*i)

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
