""" 
This program will find the minimum number of moves required by a knight on a chessboard to go to the last cell
of a chessboard.

The valid moves are:
1. (x +- a), (y +- b)
2. (x +- b), (y +- a) 

We will use BFS as we are basically finding the shortest path in an unweighted graph
"""

def bfs(a, b, n):
    queue = [(0, 0, 0)] # Starting from (0,0)

    visited = [[False for _ in range(n)] for _ in range(n)]

    # Basic BFS implementation
    while(len(queue) > 0):

        i, j, cost = queue.pop()

        # We have reached the last cell, so return the number of moves
        if(i == n - 1 and j == n - 1):
            return cost

        # All the possible moves allowed (Total of 8)
        all_moves = [
            (i + a, j + b), (i + b, j + a),
            (i - a, j - b), (i - b, j - a),
            (i - a, j + b), (i - b, j + a),
            (i + a, j - b), (i + b, j - a)
        ]

        # All the valid moves i.e., the moves that lead to a cell that is present on the chessboard
        valid_moves = [(current_i, current_j) for current_i, current_j in all_moves
        if current_i >= 0 and current_i < n and current_j >= 0 and current_j < n]

        for current_i, current_j in valid_moves:

            if(visited[current_i][current_j] == False):

                queue.insert(0, (current_i, current_j, cost + 1))

                visited[current_i][current_j] = True


    # If we don't reach the final cell despite using all the possible moves, we can't reach the last cell
    # So, return -1
    return -1

        

def knightL(n):
    ans_matrix = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    
    # We can reach the last cell FROM the last cell in just 1 move (say)
    ans_matrix[n-2][n-2] = 1

    for i in range(n - 1):
        for j in range(n - 1):

            # We can do this because the matrix (the answer) is symmetric. So, ans[i][j] = ans[j][i]
            if(ans_matrix[j][i] != 0):
                ans_matrix[i][j] = ans_matrix[j][i]

            else:
                ans_matrix[i][j] = bfs(i + 1, j + 1, n)

    return ans_matrix



def main():
    chessboard_size = int(input("Enter size of chessboard: "))
    ans_matrix = knightL(chessboard_size)

    print("The answer matrix is: ")
    for row in range(len(ans_matrix)):
        for col in range(len(ans_matrix)):
            print(ans_matrix[row][col], end = " ")
        print()

if __name__ == "__main__":
    main()