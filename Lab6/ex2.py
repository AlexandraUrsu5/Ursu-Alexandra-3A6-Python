import re

def function2(r,txt,x):
    return list(filter(lambda el:len(el)==x, re.findall(r,txt)))
                 
def main():
    print(function2("\d\d\d", "132v43689", 3))
 
main()