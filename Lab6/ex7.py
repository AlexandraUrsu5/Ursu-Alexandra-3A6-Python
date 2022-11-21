import re

def function7(cnp):
    return re.match(r"[1256]\d\d(0[1-9]|1(0-2))(0[1-9]|[1-2][0-9]|3[0-1])\d{6}$", cnp) != None

def main():
    print(function7("2780901887755"))

main()