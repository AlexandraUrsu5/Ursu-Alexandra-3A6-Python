import os

def function3(my_path):
    
    if os.path.isfile(my_path):
        with open(my_path, "rt") as f:
            file_size = os.path.getsize(my_path)
            assert (file_size >= 20), "Fisierul nu are cel putin 20 de caractere!"
            f.seek(file_size-20)
            return f.read()
    elif os.path.isdir(my_path):
        lista = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in lista:
                    lista[ext] += 1
                else:
                    lista[ext] = 1
        lista = lista.items()
        return sorted(lista, key=lambda el: el[1], reverse=True)
    else:
        raise Exception("Parametru invalid.")
    
def main():
    print(function3(os.getcwd()))
    print(function3("C:\\Users\\alexa\\Desktop\\Facultate\\Anul 3\\Python\\Lab4\\Are.txt"))
main()

