def loop(mapping):   
    list1 = list()
    value = mapping['start']
    while value not in list1:
        list1.append(value)
        value = mapping[value]
    return list1

def main():
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z',
          'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    
main()