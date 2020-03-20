#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('задание 1')
for i in range(1, 6, 1):
     print(i, '0'*i**2)
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('задание 2')
num_2 = 0
for i in range(1, 11, 1):
    a = input('выберите цифру ')
    if '5' in a:
        num_2 += 1
print(num_2)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('задание 3')
sum = 0
for i in range(100, 0, -1):
    sum = sum + i
print(sum)

# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('задание 4')
composition = 1
for i in range(1, 11, 1):
    composition *= i
print(composition)

''' для теста'''
if composition != 1*2*3*4*5*6*7*8*9*10:
    print('реализация не верна')
else: print('все верно')
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print('задание 5')
int_num_5 = 895672564
'''нужно было для ручного прогона алгоритма'''
# print(int_num//10**(len(str(int_num))-1))
# print(int_num-(int_num//10**(len(str(int_num))-1))*10**(len(str(int_num))-1))
# print(len(str(int_num)))
# int_num =int_num - int_num//100000*10**(len(str(int_num))-1)
# print(int_num)
while int_num_5 > 0:
    print(int_num_5//10**(len(str(int_num_5))-1))
    int_num_5 = int_num_5-(int_num_5//10**(len(str(int_num_5))-1))*10**(len(str(int_num_5))-1)
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
print('задание 6')
int_num_6 = 123406789
sum_6 = 0
while int_num_6 > 0:
    sum_6 += int_num_6//10**(len(str(int_num_6))-1)
    int_num_6 = int_num_6-(int_num_6//10**(len(str(int_num_6))-1))*10**(len(str(int_num_6))-1)
print(sum_6)
'''
Задача 7
Найти произведение цифр числа.
'''
print('задание 7')
int_num_7 = 123436789
mult = 1
while int_num_7 > 0:
    digit = int_num_7 % 10
    mult *= digit
    int_num_7 = int_num_7 // 10
print(mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('задание 8')
int_num_8 = 1457452554684
sum_8 = 0
while int_num_8 > 0:
    if int_num_8 % 10 == 5:
        sum_8 += 1
    int_num_8 = int_num_8//10
if sum_8 > 0:
    print('Среди цифр есть число 5, и оно встречается ', sum_8, ' раз/а')
else:
    print('Среди цифр число 5 не встречается')

# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print('задание 9')
int_num_9 = 33334537333
max_num=0
lev_num=0
print(int_num_9 % 10)
while int_num_9 > 0:
    lev_num = int_num_9 % 10
    int_num_9 = int_num_9 // 10
    if max_num < lev_num:
        max_num = lev_num
print('максимальная цифра в числе равна ', max_num)
'''
Задача 10
Найти количество цифр 5 в числе
'''
print('задание 10')
int_num_10 = 9825567864474
sum_10 = 0
while int_num_10 > 0:
    if int_num_10 % 10 == 5:
        sum_10 += 1
    int_num_10 = int_num_10//10
if sum_10 > 0:
    print('Среди цифр есть число 5, и оно встречается ', sum_10, ' раз/а')
else:
    print('Среди цифр число 5 не встречается')