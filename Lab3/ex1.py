from collections.abc import Iterable

def function1(a, b):
    
    return set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b)-set(a)

def main():
    print(function1([1, 3, 4], [4, 5, 1]))

main()
