import math

'''
4.4.1
    функция, которая последовательно вводит с клавиатуры
    два целых числа, и затем выводит их сумму, разность,
    произведение и частное.
'''
def data_processing():
    x1 = int(input('Введите число 1:'))
    x2 = int(input('Введите число 2:'))
    sumX = int(x1+x2) # сумма
    diffX = int(x1-x2) # разность
    prodX = int(x1*x2) # произведение
    divisionX = float(x1/x2) #частное
    print('Сумма чисел',x1 , 'и',x2 ,'=',sumX)
    print('Разность чисел',x1 , 'и',x2 ,'=',diffX)
    print('Произведение чисел',x1 , 'и',x2 ,'=',prodX)
    print('Частное чисел',x1 , 'и',x2 ,'=',divisionX)

'''
4.4.2. Функция, которая вводит радиус окружности,
 а выводит её периметр.
'''
def perimeter():
    num = int(input('Введите радиус окружности: '))
    res = float(2 * math.pi * num)
    print(res)

#data_processing()
perimeter()