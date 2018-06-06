def HARM_findRoot(shortest, root, chExtentions):
    for i in range(len(shortest)):
        shortest[i].insert(0,root[i])
        shortest[i].append(chExtentions[i])
    
    #if extention lower that the higest pitch of type, add 12
    notation = shortest
    for i in range(len(notation)):
        maxNot = max(notation[i][1])
        for j in range(len(notation[i][2])):
            if notation[i][2][j]<maxNot:
                notation[i][2][j] = notation[i][2][j] + 12