def Function(matrix):
    n=len(matrix)
    m = len(matrix[0])
    r=n-1
    c=0
    list = []
    while r > 0:
        c=0
        while c < m:
            pre_r = r-1
            ok = True
            while pre_r > 0 and ok == True:
                if matrix[pre_r][c] >= matrix[r][c]:
                    list.append(tuple((r,c)))
                    ok=False
                pre_r = pre_r - 1
            c = c + 1
        r = r - 1
    return list

def main():
    matrix=[[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 7, 2],
            [5, 5, 2, 5, 6, 4],
            [6, 6, 7, 6, 7, 5]]
    print(Function(matrix))

main()