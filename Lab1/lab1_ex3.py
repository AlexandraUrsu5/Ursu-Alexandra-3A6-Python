#3
first_string = input()
second_string = input()

def occ_counter(_first_string, _second_string):
    counter = 0
    for idx in range(len(_second_string) - len(_first_string) + 1):
        if _second_string[idx:idx+len(_first_string)] == _first_string:
            counter += 1
    return counter

print(occ_counter(first_string, second_string))