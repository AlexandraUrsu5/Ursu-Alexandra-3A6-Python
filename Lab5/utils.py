import math 
def process_item(n):
	prime=0
	n+=1
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			prime=0
			break
		else:
			prime=1
	if prime==1:
		return n
	else:
		return process_item(n)

def main():

    x = int(input("x = "))
    print(process_item(x))

main()
