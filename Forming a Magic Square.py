def magic(matrix):
    values =  [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8]
        ]

    count_arr = []
    for i in range(8):
        temp = values[i]
        temp_count = 0
        for j in range(len(temp)):
            temp_count += abs(temp[j] - matrix[j])
        count_arr.append(temp_count)
    return (min(count_arr))

if __name__=="__main__":
    matrix = []
    for i in range(3):
        a,b,c = input().split()
        matrix.append(a)
        matrix.append(b)
        matrix.append(c)
    matrix = list(map(int,matrix))
    moves = magic(matrix)
    print(moves)
