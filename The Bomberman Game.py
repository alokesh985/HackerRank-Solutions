def destroy(grid,i):
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            
            if(grid[x][y] == i):
                grid[x][y] = '.'

                if(len(grid) == 1):
                    if(y == 0):
                        if(grid[x][y+1] != i):
                            grid[x][y+1] = '.'
                    
                    elif(y == len(grid[0])-1):
                        if(grid[x][y-1] != i):
                            grid[x][y-1] = '.'

                    else:
                        if(grid[x][y-1] != i):
                            grid[x][y-1] = '.'
                        if(grid[x][y+1] != i):
                            grid[x][y+1] = '.'

                elif(len(grid[0]) == 1):
                    if(x == 0):
                        if(grid[x+1][y] != i):
                            grid[x+1][y] = '.'
                    elif(x == len(grid)-1):
                        if(grid[x-1][y] != i):
                            grid[x-1][y] = '.'

                    else:
                        if(grid[x+1][y] != i):
                            grid[x+1][y] = '.'
                        if(grid[x-1][y] != i):
                            grid[x-1][y] = '.'

                elif(x == 0 and y == 0):
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'
                    

                elif(x == 0 and y == len(grid[0])-1):
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'

                elif(x == len(grid)-1 and y == 0):
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'

                elif(x == len(grid)-1 and y == len(grid[0])-1):
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'

                elif(x == 0):
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'

                elif(x == len(grid)-1):
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'

                elif(y == 0):
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'

                elif(y == len(grid[0])-1):
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'

                else:
                    if(grid[x+1][y] != i):
                        grid[x+1][y] = '.'
                    if(grid[x-1][y] != i):
                        grid[x-1][y] = '.'
                    if(grid[x][y+1] != i):
                        grid[x][y+1] = '.'
                    if(grid[x][y-1] != i):
                        grid[x][y-1] = '.'

    return grid
                

# Complete the bomberMan function below.
def bomberMan(n, grid):

    if(n == 1):
        return grid

    for i in range(len(grid)):
        grid[i] = list(grid[i])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 'O'):
                grid[i][j] = 1

    det = 3
    to_dest = 1

    res = []

    if((n % 2) == 0):
        select = 2
    if(n % 4 == 3):
        select = 3
    if(n % 4 == 1):
        select = 5

        
    for i in range(2,6):

        if(i == det):

            grid = destroy(grid,to_dest)
            if(i == 3):
                to_dest += 1
            else:
                to_dest += 2
            det += 2
            if(i == select):
                break
            continue

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if(grid[x][y] == '.'):
                    grid[x][y] = i

        if(i == select):
            break

    print(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != '.'):
                grid[i][j] = 'O'

    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
                
    return grid
