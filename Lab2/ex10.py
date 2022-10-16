def MaxLenght(lists):
    max_len = 0
    for list in lists:
        if max_len < len(list):
            max_len = len(list)
    return max_len

def Function(lists):
    max_len=MaxLenght(lists)
    final_lists = []
    for i in range(max_len):
        final_lists.append([])
    print(final_lists)
    index = 0
    for final_list in final_lists:
        ind=0
        while ind < len(lists):
            list=lists[ind]
            if index >= len(list):
                final_list.append(None)
            else:
                final_list.append(list[index])
            ind = ind + 1
        index = index + 1
    
    return final_lists
    
    
def main():
    lists = [ [1,2,3], [5,6,7], ["a", "b", "c", "d"] ]
    print(Function(lists))
    
main()
    