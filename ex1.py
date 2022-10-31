import os

def function1(director):
    try:
        list = sorted(list(set([os.path.splitext(el)[1][1:] for el in os.listdir(director) if os.path.isfile(os.path.join(director, el)) and os.path.splitext(el)[1] != ""])))
        return list                                 
    except Exception as e:
        return e
def main():
    print(function1(os.getcwd()))
main()
