def stringSimilarity(s):
    
    z = [0] * len(s)

    l, r = 0, 0

    for k in range(1,len(s)):

        if(k > r):
            l = k
            r = k

            while(r < len(s) and s[r] == s[r - l]):
                r += 1

            z[k] = r - l

            r -= 1

        else:
            #Inside Z Box
            temp = k - l
            #If value does not go out of bound s of Z box, just copy values
            if(z[temp] < r - k + 1):
                z[k] = z[temp]

            else:
                #Again compare if stretching outside Z box
                l = k
                while(r < len(s) and s[r] == s[r-l]):
                    r += 1

                z[k] = r - l
                r -= 1

    return(sum(z) + len(s))
