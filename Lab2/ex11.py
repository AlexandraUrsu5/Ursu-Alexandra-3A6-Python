def Sort(lists):
    return sorted(lists, key=lambda x: x[1][2])

def main():
    lists = [('abc', 'bcd'), ('abc', 'zzz'), ('abc', 'zza')]
    print(Sort(lists))
    
main()