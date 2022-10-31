import os

def function5(target, to_search):
    def file_contains_to_search(target, to_search):
        with open(target, "rt") as f:
            text = f.read()
            return to_search in text

    if (os.path.isfile(target)):
        if file_contains_to_search(target, to_search):
            return [target]
        else:
            return []
    elif (os.path.isdir(target)):
        result = []
        for root, dirs, files in os.walk(target):
            for f in files:
                name = os.path.join(root, f)
                if file_contains_to_search(name, to_search):
                   result += [name]
        return result
    else:
        raise ValueError("Target trebuie să fie fișier/director.")

def main():
    print(function5("c:\\Users\\alexa\\Desktop\\Facultate\\Anul 3\\Python\\Lab4","are mere"))
main()