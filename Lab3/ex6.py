def function6(lista):
    return len(set(lista)), len(lista) - len(set(lista))

def main():
    print(function6([2, 2, 3, 5, 6, 6]))
    
main()