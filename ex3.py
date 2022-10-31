import os

def function3(my_path):
    
    if os.path.isfile(my_path):
        f= open(my_path, "r")
        file_size = os.path.getsize(my_path) -20
        assert (file_size >= 0), "Fisierul nu are cel putin 20 de caractere!"
        f.seek(file_size)
        return f.read()
    elif os.path.isdir(my_path):
        list = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension in list:
                    list[extension] += 1
                else:
                    list[extension] = 1
        list = list.items()
        return sorted(list, key=lambda el: el[1], reverse=True)
    
def main():
    print(function3(os.getcwd()))
    print(function3("C:\\Users\\alexa\\Desktop\\Facultate\\Anul 3\\Python\\Lab4\\Are.txt"))
main()

