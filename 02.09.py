#1)
nums=[1,2,3,4,5]
nums=[10,20,30]
nums=[7,3,8,2]
sum=0
for i in nums:
    sum+=i
print(sum)
#2
nums=[10, 25, 7, 42, 18] 
nums=[5, 2, 9, 1]
nums=[100, 50, 75, 25] 
largest=nums[0]
for i in nums:
    if i>largest:
        largest=i
print(largest)
#3
nums=[1, 2, 3, 4, 5, 6] 
nums=[10, 15, 20, 25, 30] 
nums=[1, 3, 5, 7] 
even=0
for i in nums:
    if i%2==0:
        even+=1
print(even)
#4
nums=[-2, 5, 7, -1, 3] 
nums=[10, -5, 0, 8, -2] 
nums=[-1, -2, -3] 
count=0
for i in nums:
    if i >0:
        count+=1
print(count)
#5
nums=[1, 2, 3, 4, 5] 
nums=[10, 20, 30] 
nums=[30, 20, 10] 
print(nums[::-1])
#6
nums=[8, 3, 12, 5, 1] 
nums=[20, 15, 30, 10]
nums=[-5, -2, -10, -1]  
sm=nums[0]
for i in nums:
    if i<sm:
        sm=i
print(sm)
#7
nums= [1, 2, 2, 3, 2, 4]
nums=[5, 5, 1, 2, 5]  
nums=[10, 20, 30]
tr=5
count=0
for i in nums:
    if i==5:
        count+=1
print(count)

#8
nums=[1, 2, 3, 4, 5] 
nums=[10, 15, 20, 25, 30] 
nums=[2, 4, 6, 8] 
odd=[]
for i in nums:
    if i%2!=0:
        odd.append(i)
print(odd)
#9
nums=[10, 20, 30, 40] 
nums=[5, 10, 15] 
nums=[2, 4] 
lenn=len(nums)
sum=0
avg=0
for i in nums:
    sum+=i
avg=sum/lenn
print(avg)
#10
nums=[10, 20, 30, 40] 
tr=30
for i in nums:
    if tr==i:
        print(True)
#11
nums=[10,20,5,30,25]
nums=[4, 8, 2, 10, 6] 
nums=[15, 15, 10, 20, 5] 
largest=nums[0]
second_largest=None
for i in nums:
    if i>largest:
        second_largest=largest
        largest=i
    elif i!=largest:
        if second_largest is None or i>second_largest:
            second_largest=i
print(second_largest)
#12
nums=[1, 2, 2, 3, 1, 4] 
nums=[5, 5, 5, 2, 2, 1] 
nums=[10, 20, 10, 30, 20] 
emty=[]
for i in nums:
    if i not in emty:
        emty.append(i)
print(emty) 
#13
nums=[0, 1, 0, 3, 12] 
nums=[1, 0, 2, 0, 4, 5] 
nums=[0, 0, 1, 2] 
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        j+=1
print(nums)
#14
nums=[3, 0, 1] 
nums=[0, 1] 
nums=[9, 6, 4, 2, 3, 5, 7, 0, 1] 
n=len(nums)
n1=n*(n+1)//2
sum=0
for i in nums:
    sum+=i
missing=n1-sum
print(missing)
#15
list1= [1, 2, 3, 4] 
list2= [3, 4, 5, 6] 
list1= [10, 20, 30] 
list2=[20, 30, 40] 
list1= [1, 2, 3] 
list2= [4, 5, 6] 

empty=[]
for i in list1:
    for j in list2:
        if i==j:
           empty.append(i)
print(empty)
#16
nums=[3,2,3]
nums=[2, 2, 1, 1, 1, 2, 2] 
nums=[5, 5, 5, 2, 3, 5, 4] 
element=[]
count=0
for i in nums:
    if count==0:
        element=i
    if i ==element:
        count+=1
    else:
        count-=1
print(element)
#17
nums=[2, 7, 11, 15] 
nums= [3, 2, 4] 
target=6
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target :
            print(nums[i], nums[j])
#18
nums=[-2, 5, -7, 8, 0, 3] 
nums=[10, -5, -2, 7, 4]
nums=[-1, -2, -3, 0] 
positive=[]
negative=[]
for i in nums:
    if i >0:
        positive.append(i)
    else:
        if i<0:
         negative.append(i)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
#19
lst = [10, 5, 3, 4, 3, 5]

for i in range(len(lst)):
    if lst[i] in lst[:i]:
        print(lst[i])
        break
#20
lst = [1, 2, 3, 4, 5, 6, 7]
k = 3

k = k % len(lst)

lst = lst[-k:] + lst[:-k]

print(lst)





