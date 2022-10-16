def ASCII(x, strings, flag):
    lists = []
    for string in strings:
        list = []
        for ch in string:
            if flag and ord(ch)%x == 0:
                    list.append(ch)
            if flag == False and ord(ch)%x != 0:
                    list.append(ch)
        lists.append(list)
    return lists

def main():
    x = 2
    lists = ["test", "hello", "lab002"]
    flag = False
    print(ASCII(x,lists, flag))
    
main()