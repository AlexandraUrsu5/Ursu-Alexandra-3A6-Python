import os

def function7(fisier):
    try:
        assert (os.path.isfile(fisier)
                ), "Parametrul trebuie să fie o cale de fișier"
        return {"full_path": os.path.abspath(fisier),
                "file_size": os.path.getsize(fisier),
                "file_extension": os.path.splitext(fisier)[1],
                "can_read": os.access(fisier, os.R_OK),
                "can_write": os.access(fisier, os.W_OK)}
    except Exception as e:
        print(str(e))
        return {}
    
def main():
    print(function7("c:\\Users\\alexa\\Desktop\\Facultate\\Anul 3\\Python\\Lab4\\fisier.txt"))
main()
