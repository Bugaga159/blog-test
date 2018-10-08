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
    divisionX = int(x1/x2*100)/100 #частное
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
'''
    4.4.3 
    Функция выводит ровное дробное число,
    при вводе три дробных числа 
'''
def res_input_numbers():
    x1 = float(input('Введите число: '))
    x2 = float(input('Введите число: '))
    x3 = float(input('Введите число: '))
    res = int((x1+x2+x3)/3*100)/100
    print('Ровное дробное число =',res)

'''
    4.4.5 
    Функция выводит сумму числа переменной n, в формате n+nn+nnn
'''
def encryption_num():
    num1 = int(input('Введите число для шифрования: '))
    num2 = num1
    n = 0
    b = 3
    res2 = 0
    while num2 != 0:
        num2 = int(num2/10)
        n += 1
    res1 = num1 + int(num1 * (10 ** n)) + int(num1 * ((10 ** n) ** 2))
    while b != 0:
        res2 += res1
        res1 = int( res1 / (10**n))
        b -= 1
    print(res2)

encryption_num()