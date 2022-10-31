import sys
import os

def function4():
    try:
        assert (os.path.isdir(sys.argv[1])), "Directorul nu exista."
        return sorted(list(set([os.path.splitext(el)[1][1:] for el in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], el)) and os.path.splitext(el)[1] != ""])))
    except Exception as e:
        print(str(e))
        return []
    
def main():
    print(function4())
main()

# python ex4.py c:\\Users\\alexa\\Desktop\\Facultate