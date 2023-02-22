'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
пример
5
1 2 3 4 5
6
-> 5'''

from random import randint

length = int(input('Введите длину массива: '))
x = int(input('Введите число: '))
st = list(randint(1, 99) for i in range(length))

print(st)

st1 = []
for e in st:
     if e >= x:
         st1.append(e - x)
     else:
         st1.append(x - e)
print(st1)

mini = 0
for i in range(len(st1)):
     if st1[i] < st1[mini] and st1[i] != 0:
         st1[mini] = st1[i]
         ind = i

print(f'Самое приблеженное значение {st1[ind]}')
