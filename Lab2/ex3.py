def Intersection(list1, list2):
	return list(set(list1).intersection(list2))

def Union(list1, list2):
	final_list = list(set(list1) | set(list2))
	return final_list

def Difference(list1, list2):
    list_difference = list(set(list1) - set(list2))
    return list_difference

def Function(list1, list2):
    print(Intersection(list1, list2))
    print(Union(list1, list2))
    print(Difference(list1, list2))
    print(Difference(list2, list1))

def main():
    list1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
    list2 = [9, 9, 74, 21, 45, 11, 63]
    Function(list1, list2)
main()