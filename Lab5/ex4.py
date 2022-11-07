def function4(*args, **dicts):
    list = []
    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 
                                             else False
                                             for key in arg.keys()]):
                list.append(arg)

    for key in dicts.keys():
        if type(dicts[key]) == dict:
            if len(dicts[key].keys()) >= 2 and any([True if type(ky) == str and 
                                                    len(ky) >= 3 else False
                                                    for ky in dicts[key].keys()]):
                list.append(dicts[key])
    return list


def main():
    print(function4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5},
                 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    
main()
