def is_diagonal(x):
    y=0
    i=0
    while(True):
        if(x[i][i]==x[i+1][i+1]):
            y+=1
        else:
            y-=1
        i+=1
        if(i==(len(x)-1)):
            break
    i=0
    if((len(x)-1)!=y):
        while(True):
            if(x[len(x)-2-i][len(x)-2-i]==x[len(x)-1-i][len(x)-1-i]):
                y+=1
            else:
                y-=1
            i+=1
            if(i==(len(x)-1)):
                break
    if((len(x)-1)==y):
        return True
    else:
        return False
print(is_diagonal([[1,0,0],[0,1,0],[0,0,1]]))