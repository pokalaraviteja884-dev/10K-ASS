# 1. Print Numbers from 1 to n

n = 5

for i in range(1, n + 1):
    print(i, end=" ")

print("\n")


# 2. Print Numbers from m to n

m = 3
n = 7

for i in range(m, n + 1):
    print(i, end=" ")

print("\n")


# 3. Print Numbers from n to 1 in Reverse

n = 5

for i in range(n, 0, -1):
    print(i, end=" ")

print("\n")


# 4. Print Numbers from n to m in Reverse

n = 10
m = 6

for i in range(n, m - 1, -1):
    print(i, end=" ")

print("\n")


# 5. Sum of n Natural Numbers

n = 5
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)


# 6. Factorial of a Number

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# 7. Sum of m to n Numbers

m = 3
n = 6
total = 0

for i in range(m, n + 1):
    total = total + i

print("Sum =", total)


# 8. Product of m to n Numbers

m = 2
n = 4
product = 1

for i in range(m, n + 1):
    product = product * i

print("Product =", product)


# 9. Print Factors of a Number

n = 6

print("Factors:", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

print()


# 10. Count of Factors

n = 6
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

print("Number of Factors =", count)


# 11. Prime Number Check

n = 7
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# 12. Even Numbers from m to n

m = 3
n = 10

print("Even Numbers:", end=" ")

for i in range(m, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()


# 13. Odd Numbers from m to n

m = 3
n = 10

print("Odd Numbers:", end=" ")

for i in range(m, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

print()


# 14. Count Even and Odd Numbers

m = 3
n = 7

even = 0
odd = 0

for i in range(m, n + 1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)


# 15. Reverse a String

text = "hello"
reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

print("Reverse =", reverse)


# 16. Check Palindrome String

text = "madam"
reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 17. Sum of Digits

n = 123
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of Digits =", total)


# 18. Product of Digits

n = 123
product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print("Product of Digits =", product)


# 19. Armstrong Number

n = 153
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit * digit * digit
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")


# 20. Reverse a Number

n = 123
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse Number =", reverse)


# 21. Palindrome Number

n = 121
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# 22. Count Vowels

text = "apple"
count = 0

for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1

print("Vowels =", count)


# 23. Count Consonants

text = "apple"
count = 0

for ch in text:
    if ch.isalpha():
        if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u':
            count = count + 1

print("Consonants =", count)


# 24. Count Vowels and Consonants

text = "apple"

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():

        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)


# 25. Perfect Number

n = 28
total = 0

for i in range(1, n):
    if n % i == 0:
        total = total + i

if total == n:
    print("Perfect number")
else:
    print("Not Perfect number")


# 26. Neon Number

n = 9

square = n * n
total = 0

while square > 0:
    digit = square % 10
    total = total + digit
    square = square // 10

if total == n:
    print("Neon number")
else:
    print("Not Neon number")


# 27. Strong Number

n = 145
temp = n
total = 0

while temp > 0:

    digit = temp % 10

    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10

if total == n:
    print("Strong number")
else:
    print("Not Strong number")


# 28. Harshad Number

n = 18
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

if n % total == 0:
    print("Harshad number")
else:
    print("Not Harshad number")


# 29. Fibonacci Series

n = 5

a = 0
b = 1

print("Fibonacci:", end=" ")

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()


# 30. Neon Number Again

n = 9

square = n * n
total = 0

while square > 0:
    digit = square % 10
    total = total + digit
    square = square // 10

if total == n:
    print("Neon number")
else:
    print("Not Neon number")