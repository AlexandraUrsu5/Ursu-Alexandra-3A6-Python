from math import*

def isPrime(n):

	if (n <= 1):
		return False
	if (n == 2 or n == 3):
		return True
	if (n % 2 == 0 or n % 3 == 0):
		return False
	for i in range(5, floor(sqrt(n)), 6):
		if (n % i == 0 or n % (i + 2) == 0):
			return False
	return True

def is_primes(list):
    primes = []
    for e in list:
        if isPrime(e):
            primes.append(e)
    return primes
	
    
def main():
    list = [2,4,6,3]
    print(is_primes(list))
main()

