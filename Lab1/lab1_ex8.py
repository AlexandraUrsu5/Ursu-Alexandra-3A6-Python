number = int(input())
binary = bin(number)
count = 0

for i in binary:
    if(i=='1'):
        count=count+1
print(count)