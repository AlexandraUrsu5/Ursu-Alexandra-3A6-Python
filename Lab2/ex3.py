def intersec(list1, list2):
	return list(set(list1).intersection(list2))

def union(list1, list2):
	final_list = list(set(list1) | set(list2))
	return final_list

def difference(list1, list2):
    list_difference = list(set(list1) - set(list2))
    return list_difference

def function(list1, list2):
    print(intersec(list1, list2))
    print(union(list1, list2))
    print(difference(list1, list2))
    print(difference(list2, list1))

def main():
    list1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
    list2 = [9, 9, 74, 21, 45, 11, 63]
    function(list1, list2)
main()