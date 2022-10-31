import os

def function2(director, fisier):
    try:
        with open(fisier, "w") as f:
            for el in os.listdir(director):
                name = os.path.join(director, el)
                if os.path.isfile(name) and el.startswith("A"):
                    f.write(os.path.abspath(name)+os.linesep)
    except Exception as e:
        print(str(e))
def main():
    function2(os.getcwd(), "fisier.txt")
main()
