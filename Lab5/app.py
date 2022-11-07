import utils

def main():
    while True:
        x = input("x = ")
        if x == "q":
            return
        try:
            x = int(x)
        except Exception as e:
            print("x is not intreger.")
        else:
            print(utils.process_item(x))
main()