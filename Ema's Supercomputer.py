def twoPluses(grid):

    ans = 1
    ''' To solve this problem, we have to chech each and every non-overlapping pair of squares of ALL SIZES. So we take
    all possible combinations for the first square and then try to find all possible combinations for the second square '''

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):

            z = 0

            while(grid[i+z][j] == 'G' and grid[i-z][j] == 'G' and grid[i][j+z] == 'G' and grid[i][j-z] == 'G'):
                
                # Marking square units to avoid overlapping
                grid[i+z][j] = grid[i-z][j] = grid[i][j+z] = grid[i][j-z] = 'U'

                for I in range(1, len(grid) - 1):
                    for J in range(1, len(grid[0]) - 1):

                        Z = 0
                        while(grid[I+Z][J] == 'G' and grid[I-Z][J] == 'G' and grid[I][J+Z] == 'G' and grid[I][J-Z] == 'G'):
                            ans = max(ans, ((4*z)+1) * ((4*Z)+1))

                            # Checking if any boundary is getting crossed 
                            if(I+Z == len(grid) - 1 or I-Z == 0 or J+Z == len(grid[0]) - 1 or J-Z == 0):
                                break
                            else:
                                Z += 1
                
                # Checking if any boundary is getting crossed 
                if(i+z == len(grid) - 1 or i-z == 0 or j+z == len(grid[0]) - 1 or j-z == 0):
                    break
                else:
                    z += 1

            z = 0
            while(grid[i+z][j] == 'U' and grid[i-z][j] == 'U' and grid[i][j+z] == 'U' and grid[i][j-z] == 'U'):
                
                grid[i+z][j] = grid[i-z][j] = grid[i][j+z] = grid[i][j-z] = 'G'
                
                # Checking if any boundary is getting crossed 
                if(i+z == len(grid) - 1 or i-z == 0 or j+z == len(grid[0]) - 1 or j-z == 0):
                    break
                else:
                    z += 1
    
    return ans
