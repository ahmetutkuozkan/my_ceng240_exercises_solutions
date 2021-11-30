def countdown(x,y):
    result=0
    for i in range(len(y)):
        if(x>y[i]):
            result+=1
            x-=y[i]
        else:
            break
    return result
