import re


def censures(s):
    word = s.group(0)
    vowels = "aeiou"
    if re.match("[aeiou]",word):
        return s.group(0)
    return "".join([ch if idx % 2 == 0 else '*' for idx, ch in enumerate(s.group(0))])

def function6(txt):
    return re.sub("\w+",censures,txt)

def main():
    print(function6("Ana are mere si afine."))
main()