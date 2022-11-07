def using_function(text):
    return [ch for ch in text if ch.lower() in "aeiou"]

anon_function = lambda text: [ch for ch in text if ch.lower() in "aeiou"]

def using_filter(string): 
    return list(filter(lambda x: x.lower() in "aeiou", string))

def main():
    print(using_function("Programming in Python is fun"))
    print(anon_function("Programming in Python is fun"))
    print(using_filter("Programming in Python is fun"))

main()