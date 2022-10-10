def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for ch in str:
        if ch in vowel:
            count = count + 1

    print("No. of vowels:", count)


str = "Ana are mere"
vowel_count(str)