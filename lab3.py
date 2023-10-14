import random

#Task 1
num = int(input('enter your number for 1st task: '))
i=1
arr=[]
while i<=num:
    if i%2==0: 
        arr.append(i)
    i+=1
print(arr)

# Task 2
factorial=1
num_2 = int(input('enter your number for 2nd task: '))
while i<=num_2:
    factorial*=i
    i+=1
print(factorial)

#Task 3
while True:
    num_3 = int(input('enter your number for 3rd task: '))
    if num_3==42:
        print('This number is 42')
        break
    else:
        print('This is wrong number')
        # 5. Сумма цифр числа (строковые операции).
# //                Попросите пользователя ввести число, затем найдите и выведите сумму его цифр.


sum_of_digits = input("Введите число: ")
sum = 0

for i in range(len(sum_of_digits)):
    digit = sum_of_digits[i]
    if digit.isdigit():
        num_digit = int(digit)
        sum += num_digit

print(sum)

# //        6. Числа Фибоначчи (пока). Напишите программу для печати первых N чисел Фибоначчи,
# //                где N - положительное целое число, введенное пользователем. Используйте цикл while.

fibonacci = int(input("Введите количество членов последовательности Фибоначчи: "))
sum = 0
i = 0
f1 = 0
f2 = 1
print(f1)
print(f2)

while i < fibonacci - 2:
    i += 1
    sum = f1 + f2
    f1 = f2
    f2 = sum
    print(sum)

# 7. Переверните строку (операции со строками). Попросите пользователя ввести str.
# //        вводим, а затем выводим его в обратном порядке.

str2 = input("Введите строку: ")
sum_str = ""

for i in range(len(str2) - 1, -1, -1):
    sum_str += str2[i]

print(sum_str)

# //        8. Пропустите четные (продолжайте).
# //                Напишите программу, которая предложит пользователю ввести цифры, и если введенное число четное,
# //        оно будет пропущено с помощью конструкции continue. Программа должна вывести сумму всех нечетных чисел.

sum = 0

while True:
    numberrr = int(input("write a numberrr"))

    if numberrr == 0:
        break
    if numberrr % 2 == 0:
        continue

    sum += numberrr

print(sum)


# 9. Угадайте число (перерыв). Напишите игру, в которой компьютер выбирает случайное число от 1 до 100,
# //            а пользователь должен угадать это число.
# //                Программа должна отображать подсказки ("Слишком маленький" или "Слишком большой") и завершать работу,
# //                когда пользователь угадает число. Используйте конструкцию break, чтобы завершить игру.


randnum = random.randint(1,100)
print(randnum)

while True:
    numwin = int(input("write a num \n"))
    if randnum > numwin:
        print("число больше чем это")
    if randnum < numwin:
        print("число меньше чем это")
    if randnum == numwin:
        print("winnn!!!")
        break


# //        10. Палиндром (строковые операции). Попросите пользователя ввести строку и определить,
# //                является ли она палиндромом (читайте то же самое справа налево, что и слева направо).

str222 = input("Введите строку: ")
pal = ""

for i in range(len(str222) - 1, -1, -1):
    pal += str222[i]

if pal == str222:
    print("Палиндром")
else:
    print("Не палиндром")


# //        11. Пронумеруйте до степени (пока). Напишите программу,
# //            которая предлагает пользователю ввести число X и степень Y.
# //        Затем вычислите и выведите X в степени Y, используя цикл while.

x = int(input("Введите число \n"))
y = int(input("Введите степень \n"))
i = 1;
summm = 1;
while i <= y:
    i+=1
    summm*=x

print(summm)


# 12. Подсчет простых чисел (While, Break).
# Напишите программу, которая найдет и напечатает все простые числа в диапазоне от 1 до N,
# //        где N - положительное целое число, введенное пользователем.
# Используйте цикл while и конструкцию break для оптимизации процесса.


n = int(input("Введите число n: "))
i = 2

while i <= n:
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
    i += 1


# 13. Обратное число (строковые операции). Попросите пользователя ввести номер и напечатать его в обратном порядке.
number = input("Введите число: ")
reversed_number = number[::-1]
print("Число в обратном порядке:", reversed_number)



# //        14. Проверьте на первичность (продолжайте).
# //                Напишите программу, которая проверяет, является ли число,
# //        введенное пользователем, простым числом. Если число не является простым,
# //                программа должна напечатать следующее простое число и продолжить тестирование. Используйте конструкцию continue.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Введите число для проверки на простоту: "))

while True:
    if is_prime(number):
        print(f"{number} - простое число.")
        break
    else:
        print(f"{number} не является простым числом.")
        number += 1

# //        15. Шифр Цезаря (строковые операции).
# //        Попросите пользователя ввести строку и сдвинуть все буквы в строке на N позиций вперед по алфавиту (циклически),
# //                где N - целое число, введенное пользователем. Выведите зашифрованную строку.

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

user_input = input("Введите строку: ")
shift = int(input("Введите сдвиг (целое число): "))

encrypted_text = caesar_cipher(user_input, shift)
print("Зашифрованная строка:", encrypted_text)