import os
import re

def function8(dir,reg):
    result = []
    for root,dirs,files in os.walk(dir):
        for f in files:
            file = os.path.join(root,f)
            r = re.search(reg,f)
            with open(file, "r") as file_open:
                string = file_open.read()
                if (re.search(reg, string)):
                    if r:
                        result += [">>" + f]
                    else:
                        result+=[f]
                else:
                    if r:
                        result+=[f]
    return result


def main():
    print(function8(os.getcwd(), "\d\d"))

main()
