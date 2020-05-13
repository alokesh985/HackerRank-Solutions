def gridSearch(G, P):
    
    for i in range(len(G)):
        for j in range(len(G[0])):
            if(G[i][j] == P[0][0]):
                
                if(i <= len(G)-len(P) and j <= len(G[0])-len(P[0])):
                    flag = 0
                    x = i
                    for k in range(len(P)):
                        temp1 = G[x]
                        x += 1
                        temp2 = temp1[j:j+len(P[0])]
                        if(temp2 == P[k]):
                            continue
                        else:
                            flag = 1
                            break
                    if(flag == 0):
                        return("YES")
            
    return("NO")
