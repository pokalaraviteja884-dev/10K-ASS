'''Nested for Loop — Easy Level Practice Questions

1. Print the following numbers using nested for loops:

1 2 3
1 2 3
1 2 3
'''

'''
2. Print the following:

* * *
* * *
* * *


3. Print numbers from 1 to 5 in 3 rows:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5


4. Print the following pattern:

1 1 1
2 2 2
3 3 3


5. Print the following pattern:

1 2
1 2
1 2
1 2


6. Print a 4 × 4 square of *:

* * * *
* * * *
* * * *
* * * *


7. Print the multiplication tables from 1 to 3, with each table containing numbers from 1 to 5.


8. Print all numbers from 1 to 9 in the following format:

1 2 3
4 5 6
7 8 9


9. Print the following pattern:

A A A
B B B
C C C


10. Print the following pattern:



A B C
A B C
A B C

11. Print the numbers from 1 to 4 in 4 rows, where each row contains the same number.


12. Print the following pattern:



* *
* *
* *
* *
* *

13. Print a 5 × 5 grid containing numbers from 1 to 5 in every row.


14. Print the following pattern:



1
2 2
3 3 3

15. Print the following pattern:



*
* *
* * *

16. Print the following pattern:



1
1 2
1 2 3

17. Print the following pattern:



A
A B
A B C

18. Print the following pattern:



1 2 3 4
1 2 3
1 2
1

19. Print the following pattern:



* * * *
* * *
* *
*

20. Print the following pattern:



1
2 3
4 5 6

21. Print a 3 × 3 multiplication table.


22. Print the following:



1 2 3 4
2 3 4 5
3 4 5 6

23. Print the following:



5 5 5 5
4 4 4 4
3 3 3 3
2 2 2 2
1 1 1 1

24. Print the following pattern:



A B
C D
E F

25. Print a rectangle of * having 3 rows and 5 columns.'''
#1
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

#2
for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")
    print()

#3
for i in range(1,4):
    for j in range(1,6):
        print( j ,end= " ")
    print()

#4
for i in range(1,4):
    for j in range(1,4):
        print( i ,end=" ")
    print()

#5
for i in range(1,5):
    for j in range(1,3):
        print( j ,end= " ")
    print()

#6
for i in range(1,5):
    for j in range(1,5):
        print( "*",end= " ")
    print()

#7
for i in range(1,4):
    for j in range(1,6):
        print( i*j ,end=" ")
    print()

#8
n=1
for i in range(1,4):
    for j in range(1,4):
        print( n ,end= " ")
        n=n+1
    print()

#9
for i in range(1,4):
    for j in range(1,4):
        print( chr(64+i) , end=" ")
    print()

#10
for i in range(1,4):
    for j in range(1,4):
        print( chr(64+j) ,end= " ")
    print()

#11
for i in range(1,5):
    for j in range(1,5):
        print( i ,end= " ")
    print()
#12
for i in range(1,6):
    for j in range(1,3):
        print( "*",end= " ")
    print()
#13
for i in range(1,6):
    for j in range(1,6):
        print( j,end= " ")
    print()

#14
for i in range(1,4):
    for j in range(1,i+1):
        print( i,end= " ")
    print()

#15
for i in range(1,4):
    for j in range(1,i+1):
        print( '*',end= " ")
    print()

#16
for i in range(1,4):
    for j in range(1,i+1):
        print( j,end= " ")
    print()

#17
for i in range(1,4):
    for j in range(1,i+1):
        print( chr(64+j),end= " ")
    print()

#18
for i in range(4,0,-1):
    for j in range(1,i+1):
        print( j,end= " ")
    print()

#19
for i in range(3,0,-1):
    for j in range(1,i+1):
        print( '*',end= " ")
    print()

#20
n=1
for i in range(1,4):
    for j in range(1,i+1):
        print( n,end= " ")
        n=n+1
    print()

#21
for i in range(1,4):
    for j in range(1,4):
        print( i*j,end= " ")
    print()

#22
for i in range(1,4):
    for j in range(1,5):
        print( i+j-1,end= " ")
    print()

#23
for i in range(5,0,-1):
    for j in range(4):
        print( i,end= " ")
    print()

#24
value=65
for i in range(3):
    for j in range(2):
        print(chr(value),end=" ")
        value+=1
    print()

#25
for i in range(1,4):
    for j in range(1,6):
        print( '*',end= " ")
    print()


