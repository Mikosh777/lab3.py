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

#Task 4
str1 = input("Enter string for 4th task: ")
count = 0

for char in str1:
    if char == 'a':
        count += 1

print(count)

#Task 5.
sum_of_digits = input("enter your number for 5th task: ")
sum = 0

for i in range(len(sum_of_digits)):
    digit = sum_of_digits[i]
    if digit.isdigit():
        num_digit = int(digit)
        sum += num_digit

print(sum)

#Task 6. 
fibonacci = int(input("enter your number for Fibbonacci: "))
sum = 0
i = 0
f1 = 0
f2 = 1

while i < fibonacci - 2:
    i += 1
    sum = f1 + f2
    f1 = f2
    f2 = sum
    print(sum)

#Task 7. 

str2 = input("Enter string for 7th task : ")
sum_str = ""

for i in range(len(str2) - 1, -1, -1):
    sum_str += str2[i]

print(sum_str)

#Task 8.
sum = 0

while True:
    number8 = int(input("enter your number for 8th task"))

    if number8 == 0:
        break
    if number8 % 2 == 0:
        continue

    sum += number8

print(sum)


#Task 9. 


rand_num = random.randint(1,100)
print(rand_num)

while True:
    numwin = int(input("write a num \n"))
    if rand_num > numwin:
        print("num is more than this")
    if rand_num < numwin:
        print("num is less than this")
    if rand_num == numwin:
        print("You are Winner!!!")
        break


#Task10. 
str222 = input("Enter string fpr 10th task: ")
pal = ""

for i in range(len(str222) - 1, -1, -1):
    pal += str222[i]

if pal == str222:
    print("Palindrom")
else:
    print("Not polindrom")


#Task 11. 

x = int(input("Enter x: "))
y = int(input("Enter power(y): "))
i = 1
sum11 = 1
while i <= y:
    i+=1
    sum11*=x
print(sum11)


#Task 12. 
n = int(input("Enter number n: "))
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


#Task 13. 
number = input("enter your number for 13th task: ")
reversed_number = number[::-1]
print("Reserved number is:", reversed_number)



#Task 14. 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("enter your number for 14th task: "))

while True:
    if is_prime(number):
        print(f"{number} - prime number.")
        break
    else:
        print(f"{number} is not prime number.")
        number += 1

#Task 15. 

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

user_input = input("Enter string for 15 task: ")
shift = int(input("Enter shift (solid number): "))

encrypted_text = caesar_cipher(user_input, shift)
print("CypherText:", encrypted_text)
