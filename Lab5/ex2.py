def sum_values(*args, **args2):
    sum = 0
    for key in args2.keys():
        sum += int(args2[key])
    return sum

anon_function = lambda *args, **kwargs: sum([val for val in kwargs.values()])

def main():
    print(sum_values(1, 2, c=3, d=4))
    print(anon_function(1, 2, c=3, d=4))
    
main()
