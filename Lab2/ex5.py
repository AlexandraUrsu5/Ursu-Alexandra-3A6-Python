def underDiagonal(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if (i > j):
                matrix[i][j] = 0
    return matrix
    
    
def main():
    n = 3
    m = 3
    mat = [[ 2, 1, 7 ],
           [ 3, 7, 2 ],
           [ 5, 4, 9 ]]
    
    matrix = underDiagonal(mat, n, m)
    for i in range(n):
        for j in range(m):
            print(" ", matrix[i][j], end = " ")
        print(" ")
main()