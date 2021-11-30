def substring_count(x,y):
    count = 0
    for i in range(len(x)):
        if(x[i:len(y)+i]==y):
            count+=1
    return count