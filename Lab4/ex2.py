import os

def function2(director, file):
    try:
        file= open(file, "w")
        for el in os.listdir(director):
                name = os.path.join(director, el)
                if os.path.isfile(name) and el.startswith("A"):
                    file.write(os.path.abspath(name)+os.linesep)
        file.close()
    except Exception as e:
        print(str(e))
def main():
    function2(os.getcwd(), "file.txt")
main()
