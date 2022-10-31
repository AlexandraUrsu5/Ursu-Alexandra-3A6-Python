import os

def function8(dir_path):
    try:
        result = []
        for el in os.listdir(dir_path):
            if (os.path.isfile(el)):
                name = os.path.join(dir_path, el)
                result += [os.path.abspath(name)]
        return result
    except Exception as e:
        print(str(e))
        return []

def main():
    list = function8("c:\\Users\\alexa\\Desktop\\Facultate\\Anul 3\\Python\\Lab4")
    for el in list:
        print(el)
main()