def larrysArray(A):

    inversions = 0

    for i in range(len(A)):
        for j in range(i,len(A)):
            if(A[j] < A[i]):
                inversions += 1

    if(inversions % 2 == 0):
        return("YES")
    else:
        return("NO")
