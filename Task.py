#Задача 1
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

quantity = int(input('Введите количество монеток на столе: '))
list = []
count_heads = 0
count_tails = 0

print('Введите монеты: 1=орел, 0=решка')
for i in range(quantity):
    q = int(input(f'монета {i+1} --> '))
    if (q == 1):
        count_heads += 1
    else:
        count_tails += 1
    list.append(q)

print(f'Нужно перевернуть {count_heads} монет') if(count_heads < count_tails) else print(f'Нужно перевернуть {count_tails} монет')