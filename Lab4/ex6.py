import os

def function5(target, to_search):
    def file_contains_to_search(target, to_search):
        with open(target, "r") as f:
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
        raise ValueError("Target nu e fișier/director.")



def function6(target, to_search, callback):
    try:
        return function5(target, to_search)
    except Exception as e:
        return callback(e)
    
def callbackFunc(e):
    return e

def main():
    print(function6("","are mere", callbackFunc))
main()