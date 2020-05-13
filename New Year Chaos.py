def minimumBribes(q):
    flag = 0
    counter = 0
    for i in range(len(q)-1,0,-1):
        value = (i+1)

        if(q[i] != value):
            if(value == q[i-1] and i > 0):
                q[i-1], q[i] = q[i], q[i-1]
                counter += 1

            elif(value == q[i-2] and i > 1):
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1], q[i] = q[i], q[i-1]
                counter += 2

            else:
                flag = 1
                break

      

    if(flag == 1):
        print("Too chaotic")
    else:
        print(counter)
