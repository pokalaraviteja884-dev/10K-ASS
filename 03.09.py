#1
numbers = [[1, 2], [3, 4], [5, 6]] 
for i in numbers:
    for j in i:
        print(j)
#2
numbers = [[10, 20], [30, 40], [50, 60]] 
for i in numbers:
    print(i )
#3
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]] 
count=0
for i in numbers:
    for j in i:
        count+=1
print(count)
#4
numbers = [[1, 2], [3, 4], [5, 6]]
sum=0 
for i in numbers:
    for j in i:
        sum+=j
print(sum)
#5
numbers = [[10, 5], [25, 15], [8, 30]] 
largest=numbers[0][0]
for i in numbers:
    for j in i:
        if j>largest:
            largest=j
print(largest)
#6
numbers = [[10, 5], [25, 15], [8, 30]] 
smallest=numbers[0][0]
for i in numbers:
    for j in i:
        if j<smallest:
            smallest=j
print(smallest)        
#7
numbers = [[1, 2, 3], [4, 5, 6], [7, 8]]
count=0
for i in numbers:
    for j in i:
        if j%2==0:
            count+=1
print(count)
#8
numbers = [[1, 2, 3], [4, 5, 6], [7, 8]]
count=0
for i in numbers:
    for j in i:
        if j%2!=0:
            count+=1
print(count)
#9
numbers = [[10, 20], [30, 40], [50, 60]]
search = 40
for i in numbers:
    for j in i:
        if search==j:
            print("found")
#10
numbers = [[1, 2, 2], [3, 2, 4], [2, 5]] 
search = 2 
count=0
for i in numbers:
    for j in i:
        if search==j:
            count+=1
print(count)
#11
numbers = [[10, 20], [30, 40], [50, 60]] 
for i in numbers:
    for j in i:
         print(i[0])
#12
numbers = [[10, 20], [30, 40], [50, 60]]
for i in numbers:
    for j in i:
        print(i[1])
#13
numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
sum1=0
for i in numbers:
    for j in i:
        sum1+=j
    print("Sum of Each Inner List: ", sum1)
#14
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]
for i in numbers:
    largest=i[0]
    for j in i:
        if j>largest:
            largest=j
    print("Largest in Inner List: ", largest)
#15
numbers = [[10, 20, 5], [30, 15], [8, 25, 12]]
for i in numbers:
    samallest=i[0]
    for j in i:
        if j<samallest:
            samallest=j
    print("Smallest in Inner List: ", samallest)
#16
numbers = [[-2, 5, -8], [10, -3, 7], [-1, 4]] 
for i in numbers:
    for j in i:
        if j>0:
            print(j)
#17
numbers = [[5, 15, 20], [8, 25], [30, 3]]
for i in numbers:
    for j in i:
        if j>10:
            print(j)
#18
numbers = [[10, 20], [30, 40]] 
sum=0
count=0
for i in numbers:
    for j in i:
        sum+=j
        count+=1
average=sum/count
print("Average: ", average)