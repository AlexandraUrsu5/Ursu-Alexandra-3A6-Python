def fibonacci(n):
    list = []
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        list.append(a)
        return list
    elif n == 1:
        list.append(b)
        return list
    else:
        list = [0,1]
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
            list.append(b)
        return list

def main():
    n = int(input('Enter the number: '))
    print(fibonacci(n))
main()