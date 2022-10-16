from math import*

def isPrime(n):

	if (n <= 1):
		return "false"
	if (n == 2 or n == 3):
		return "true"
	if (n % 2 == 0 or n % 3 == 0):
		return "false"
	for i in range(5, floor(sqrt(n)), 6):
		if (n % i == 0 or n % (i + 2) == 0):
			return "false"
	return "true"

def main():
    n = int(input('Enter the number: '))
    print(isPrime(n))
main()

