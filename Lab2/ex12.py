def group_by_rhyme(words):
    index1 = 0
    list = []
    while index1 < len(words):
        word1 = words[index1]
        ln1 = len(word1)
        index2 = index1 + 1
        while index2 < len(words):
            word2 = words[index2]
            ln2 = len(word2)
            if word1[ln1 - 2] == word2[ln2 - 2] and word1[ln1 - 1] == word2[ln2 - 1]:
                list.append([word1, word2])
            index2 = index2 + 1
        index1 = index1 + 1
    return list

def main():
        words = ['ana', 'banana', 'carte', 'arme', 'parte']
        print(group_by_rhyme(words))
        
main()