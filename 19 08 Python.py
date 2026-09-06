'''1)n=int(input())
for i in range(1,n+1):
    print(i)'''
'''2)n=int(input())
m=int(input())
for i in range(n,m+1):
    print(i)'''
''''3)n=int(input())
for i in range(n,0,-1):
    print(i)'''
'''4)n=int(input())
m=int(input())
for i in range(n,m,-1):
    print(i)'''
'''5)n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''
'''6)n=int(input())
sum=1
for i in range(1,n+1):
    sum*=i
print(sum)'''
'''7)n=int(input())
m=int(input())
sum=0
for i in range(n,m+1):
    sum+=i
print(sum)'''
'''8)m=int(input())
n=int(input())
pro=1
for i in range(m,n+1):
    pro*=m
    m+=1
print(pro)'''
'''9)n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)'''
'''10)n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)'''
'''11)n=int(input())
count=0
for i in range(2,n+1):
    if n%i==0:
        count+=1
if count==1:
    print('prime')
else:
    print('not prime')'''
'''12)m=int(input())
n=int(input())
for i in range(m,n+1):
    if i%2==0:
        print(i)'''
'''13)m=int(input())
n=int(input())
for i in range(m,n+1):
    if i%2!=0:
        print(i)'''
'''14)m=int(input())
n=int(input())
even=0
odd=0
for i in (m,n + 1):
    if i%2==0:
        even +=1
    else:
        odd+=1
print('even =',even)  
print('odd=',odd)'''
'''15,16)n=input()
rev=''
for char in n:
    rev=char+rev
print(rev)
if rev==rev:
    print('palindrome')
else:
    print('not palindrome')
    '''
'''17)n=int(input())
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)
    '''

'''18)n=int(input())
mul=1
while n>0:
    mul*=n%10
    n//=10
print(mul)

 '''
''' 19)
number=int(input())

original_number = number

num_digits = 0
temp = number
while temp > 0:
    num_digits += 1
    temp //= 10

temp = number
digit_sum = 0
while temp > 0:
    digit = temp % 10
    digit_sum += digit ** num_digits
    temp //= 10

if digit_sum == original_number:
    print(" Armstrong number")
else:
    print(" not an Armstrong number")
'''
'''21)n=int(input())
temp=n
reversed_num = 0
while n>0:
    dig=n%10
    reversed_num=(reversed_num*10)+dig
    n//=10
if reversed_num==temp:
    print('Palindrome')
else:
    print('not Palindrome')   '''
'''22)s = input()
count = 0
for ch in s:
    if ch in "aeiou":
        count = count + 1

print(count)
'''
'''23)s = "apple"
count = 0

for ch in s:
    if ch not in "aeiou":
        count = count + 1

print(count)
'''
'''24)s = "apple"
vowels = 0
consonants=0

for ch in s:
    if ch in "aeiou":
        vowels = vowels +1
    else:
        consonants=consonants+1
  
print('vowels:',vowels,'consonants:',consonants)

'''
'''25)n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print('Perfect number')
else:
    print('not Perfect number')
'''
'''26)n = int(input())
square = n * n
sum = 0

while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == n:
    print("Neon number")
else:
    print("Not Neon number")

    '''
'''27)n = int(input())
temp = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == temp:
    print("Strong number")
else:
    print("Not Strong number")'''
'''28)
n = int(input())
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

if temp % sum == 0:
    print("Harshad number")
else:
    print("Not Harshad number")
 '''
'''29)
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    '''
'''30)
n =int(input())
square = n * n
sum = 0

while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == n:
    print("Neon number")
else:
    print("Not Neon number")
'''


