def function9(*arguments, **keywords):
    return len([element for element in arguments if element in keywords.values()])

def main():
    print(function9(1, 2, 3, 4, x=1, y=2, z=3, w=5))

main()
