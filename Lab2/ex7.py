from pickle import TRUE


def isPalindrome(number):
    reverse = int(str(number)[::-1])
    if number == reverse:
        return True
    else:
        return False

def Palindromes(numbers):
    count = 0
    max_palindrom = 0
    for number in numbers:
        if isPalindrome(number):
            count = count + 1
            if(max_palindrom<number):
                max_palindrom = number
    tupl = tuple((count,max_palindrom))
    return tupl

def main():
    numbers = [122,1221, 14441,232,23,127,343,7432] 
    print(Palindromes(numbers))

main()

