def funct_value(dict):
    dictlist=[]
    while dict !={}:
        temp = dict.popitem()
        dictlist.append(temp)
    return list(dictlist)

def function3(dict1, dict2):
    list1 = funct_value(dict1)
    list2 = funct_value(dict2)
    if list(set(list1)^set(list2)) == []:
        return True
    return False

def main():
    dict1 = {'a': 2, 'e': 3, 'A': 6, ' ': 2, 'm': 1, 'r': 2, '.': 1, 'n': 1}
    dict2 = {'a': 2, 'e': 3, 'A': 6, ' ': 2, 'm': 1, 'r': 2, '.': 1, 'n': 1}
    print(function3(dict1, dict2))
main()