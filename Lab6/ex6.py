import re

def censures(s):
    low_s = s.group(0)
    if not (low_s[0] in "aeiouAEIOU" and low_s[-1] in "aeiouAEIOU"):
        return s.group(0)
    return "".join([ch if idx % 2 == 0 else '*' for idx, ch in enumerate(s.group(0))])

def function6(txt):
    return re.sub("\w+",censures,txt)

def main():
    print(function6("Ana are mere si afine."))
main()