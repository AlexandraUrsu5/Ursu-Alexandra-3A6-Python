ok=0
text=input()
for ch in text:
    if(ch.isdigit()):
        ok=1
        print(ch, end="")
    elif(ok==1):
            break