def union(list1, list2):
    union = list(list1 + list2)
    return union

def countX(list1, x):
    final_list = []
    for e in list1:
        if list1.count(e) == x:
            final_list.append(e)
    return list(set(final_list))

def main():
    x = 2
    lists = [[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]]
    final_list = []
    for list in lists:
        final_list = union(final_list,list)
    print(final_list)
    print(countX(final_list, x))

main()
