def fibonacci_iterative(n):
    fib_list = [0] * (n + 1)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]


def fibonacci_recursive(n):

	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print("Enter a number : ")
num = int(input())
print("Iterative Fibonacci : ", fibonacci_iterative(num), "\nRecursive Fibonacci : ", fibonacci_recursive(num))

