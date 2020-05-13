def reverse_arr(arr,i,j):
    temp = arr[i:j+1]
    temp.reverse()
    x = i
    for z in range(len(temp)):
        arr[x] = temp[z]
        x += 1

    return(arr)

# Complete the almostSorted function below.
def almostSorted(arr):

    arr_sorted = sorted(arr)
    
    flag1, flag2 = 0,0

    not_in_place = 0

    if(arr == arr_sorted):
        print("yes")

    else:
        for i in range(len(arr)):
            if(flag1 == 0):
                if(arr[i] != arr_sorted[i]):
                    not_in_place += 1
                    flag1 = i+1
            
            else:
                if(arr[i] != arr_sorted[i]):
                    not_in_place += 1
                    flag2 = i+1

        if(not_in_place > 2):
            arr = reverse_arr(arr,flag1-1,flag2-1)
            if(arr == arr_sorted):
                print(f"yes\nreverse {flag1} {flag2}")
            else:
                print("no")
        else:
            arr[flag1-1], arr[flag2-1] = arr[flag2-1], arr[flag1-1]
            if(arr == arr_sorted):
                print(f"yes\nswap {flag1} {flag2}")
            else:
                print("no")
