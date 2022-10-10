text=input()
all_freq = {}
mx=0
letter=''
for ch in text:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        if ch in all_freq:
            all_freq[ch] += 1
            if(all_freq[ch]>mx):
                mx=all_freq[ch]
                letter=ch
        else:
            all_freq[ch] = 1
            if(all_freq[ch]>mx):
                mx=all_freq[ch]
                letter=ch
print(letter)