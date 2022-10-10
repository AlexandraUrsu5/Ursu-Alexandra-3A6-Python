#ex1
def gcc():
    print("Count= ")
    count = int(input())
    print("The numbers: ")
    n1 = int(input())
    cmmdc = n1
    for i in range(1, count):
        n2 = int(input())
        while n2 != cmmdc:
            if n2 > cmmdc:
                n2 = n2 - cmmdc
            else:
                cmmdc -= n2
    print(cmmdc)
gcc()