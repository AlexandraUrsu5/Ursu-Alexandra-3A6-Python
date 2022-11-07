def function5(list):
    final_list = []
    for el in list:
        if type(el) in [int, float]:
            final_list.append(el)
    return final_list


def main():
  print(function5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
  
main()
