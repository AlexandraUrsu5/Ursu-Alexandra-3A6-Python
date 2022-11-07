def function6(list_integers):
    return list(zip([i for i in list_integers if i % 2 == 0], [i for i in list_integers if i % 2 != 0]))

def main():
    print(function6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

main()
