'''Create a class named NumberSeries.
Implement a method List<Integer> getEvenNumbers(int limit) that returns all even numbers from 1 up to (and including) limit using a single for loop.
Implement a method List<Integer> getFibonacci(int count) that returns the first count Fibonacci numbers, generated with a for loop (starting with 0, 1).
Implement a method List<Integer> getPrimes(int limit) that returns all prime numbers up to limit. Use a for loop for the outer iteration and an inner for loop to test divisibility.
In each method, avoid using recursion or built‑in stream utilities; rely exclusively on explicit for loops for iteration.'''


class NumberSeries:
	def getEvenNumbers(self, n):
		even_numbers = []
		for number in range(1, n + 1):
			if number % 2 == 0:
				even_numbers.append(number)
		return even_numbers

	def getFibonacci(self, count):
		fibonacci_numbers = []
		first = 0
		second = 1

		for _ in range(count):
			fibonacci_numbers.append(first)
			first, second = second, first + second
		return fibonacci_numbers

	def getPrimes(self, n):
		primes = []
		for number in range(2, n + 1):
			is_prime = True
			for divisor in range(2, number):
				if number % divisor == 0:
					is_prime = False
					break
			if is_prime:
				primes.append(number)
		return primes
print("Even numbers up to 10:", NumberSeries().getEvenNumbers(10))
print("First 10 Fibonacci numbers:", NumberSeries().getFibonacci(10))   
print("Prime numbers up to 20:", NumberSeries().getPrimes(20))

