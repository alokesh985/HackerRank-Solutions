def balancedSums(arr):
    
    total = sum(arr)
    x = 0
    for i in range(len(arr)):
        y = arr[i]
        if((2 * x) + y == total):
            return "YES"
        x += y
        
    return "NO"
