import re

def function3(txt, list):
    return [el for el in txt if any([re.search(r, el) for r in list])]                                             
                                                  
def main():
    print(function3(['Mama', 'face','1', 'placinte.'], ["\d", "\wce", "\wte","\d", "\d{2}"])) 
      
main()                                           