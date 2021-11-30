def anagram(x,y):
    x1=[0]*len(x)
    y1=[0]*len(y)
    for i in range(len(x)):
        x1[i]=x[i]
    for i in range(len(y)):
        y1[i]=y[i]
    x1=sorted(x1)
    y1=sorted(y1)
    if(x1==y1):
        return True
    else:
        return False
