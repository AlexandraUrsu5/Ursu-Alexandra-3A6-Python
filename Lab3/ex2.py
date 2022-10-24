def function2(s):
    return {i: s.count(i) for i in s}

def main():
    print(function2("Ana are mere."))
    
main()
