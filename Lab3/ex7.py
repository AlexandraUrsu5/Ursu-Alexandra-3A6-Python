def function7(*sets):
    result = {}
    for index1 in range(0, len(sets) - 1):
        for index2 in range(index1 + 1, len(sets)):
            result.update({(str(sets[index1]) + " | " + str(sets[index2])): (sets[index1] | sets[index2]),
                           (str(sets[index1]) + " & " + str(sets[index2])): (sets[index1] & sets[index2]),
                           (str(sets[index1]) + " - " + str(sets[index2])): (sets[index1] - sets[index2]),
                           (str(sets[index2]) + " - " + str(sets[index1])): (sets[index2] - sets[index1])})
    return result

def main():
    print(function7({1, 2}, {2, 3}))
    
main()
