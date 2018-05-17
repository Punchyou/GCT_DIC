def HARM_relativeToRootExtentions(root, chExtentions):
    #move extention relatively to 0
    for i in range(len(chExtentions)):
        for j in range(len(chExtentions[i])):
            chExtentions[i][j] = chExtentions[i][j] - root[i]
            if chExtentions[i][j] <0:
                chExtentions[i][j] = chExtentions[i][j]+12
    chExtentions = root
    return root