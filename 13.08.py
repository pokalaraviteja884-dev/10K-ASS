
'''Create a class VariableSequence that internally stores a List<Integer> (or an array) supplied via constructor.
Implement a method int sum(int start, int end) that returns the sum of the elements from index start (inclusive) to end (exclusive). Assume valid indices.
Implement a method double average(int start, int length) that returns the average of a subsequence beginning at start with the specified length. Return 0.0 for an empty subsequence.
Implement a method List<Integer> maxSubsequence(int k) that returns the contiguous subsequence of length k with the greatest sum. If multiple subsequences share the maximum sum, return the first one.
Implement a method int longestIncreasingRun() that returns the length of the longest contiguous strictly increasing run within the stored sequence.
Add a method void rotate(int offset) that cyclically rotates the sequence to the right by offset positions (e.g., [1,2,3,4] rotated by 1 becomes [4,1,2,3]). The method should modify the internal storage in place.
Provide a public method List<Integer> getSequence() that returns a copy of the current sequence for inspection.'''
''''1)a=[]
n=int(input("Enter the number of elements in the list: "))
for  i in range(n):
    a.append(int(input(f"Enter element {i}: ")))
    '''
'''2
nums=[1,2,3,4,5,6,7,8]
n=len(nums)
sum=nums[0]+nums[n-1]
print("The sum of first and last element in the list is:",sum)'''
'''
3)
nums=[1,2,3,4,5,6,7,8]
length=len(nums)
start=nums[0]
total = 0
for i in range(start, start + length):
        if length == 0:
            print(0.0)
        else:
           total = total + nums[i]

print(total / length)'''
class VariableSequence:

    def __init__(self, values):
        self.sequence = list(values)

    def sum(self, start, end):
        total = 0
        for i in range(start, end):
            total += self.sequence[i]
        return total

    def average(self, start, length):
        if length == 0:
            return 0.0

        total = 0
        for i in range(start, start + length):
            total += self.sequence[i]

        return total / length

    def maxSubsequence(self, k):
        if k <= 0 or k > len(self.sequence):
            return []

        max_sum = 0
        for i in range(k):
            max_sum += self.sequence[i]

        current_sum = max_sum
        max_start = 0

        for i in range(k, len(self.sequence)):
            current_sum += self.sequence[i]
            current_sum -= self.sequence[i - k]

            if current_sum > max_sum:
                max_sum = current_sum
                max_start = i - k + 1

        result = []

        for i in range(max_start, max_start + k):
            result.append(self.sequence[i])

        return result

        
    def longestIncreasingRun(self):
        if len(self.sequence) == 0:
            return 0

        longest = 1
        current = 1

        for i in range(1, len(self.sequence)):
            if self.sequence[i] > self.sequence[i - 1]:
                current += 1
            else:
                current = 1

            if current > longest:
                longest = current

        return longest

 
    def rotate(self, offset):
        n = len(self.sequence)

        if n == 0:
            return

        offset = offset % n

        self.sequence[:] = (
            self.sequence[-offset:] +
            self.sequence[:-offset]
        )

  
    def getSequence(self):
        return self.sequence.copy()


# Example
seq = VariableSequence([1, 3, 5, 2, 4, 6, 7])

print(seq.sum(1, 4))
print(seq.average(1, 3))
print(seq.maxSubsequence(3))
print(seq.longestIncreasingRun())

seq.rotate(2)

print(seq.getSequence())

