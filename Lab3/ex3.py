from collections.abc import Iterable

#Comparați două dicționare fără a utiliza operatorul „==" care returnează Adevărat sau Fals
def return_elements(element):
    if isinstance(element, Iterable) and type(element) != str:
        #returnează True dacă obiectul specificat este de tipul specificat, în caz contrar False                              
        values = []
        if type(element) == dict:
            #returnează tipul de clasă
            for el in element.values():
                #returnează un obiect de vizualizare care conține valorile dicționarului, sub formă de listă
                values += return_elements(el)
        else:
            for el in element:
                values += return_elements(el)
        return values
    return [element]


def function3(dict1, dict2):
    return list(set(return_elements(dict1)) ^ set(return_elements(dict2)))


def main():
    print(function3())
    
main()
