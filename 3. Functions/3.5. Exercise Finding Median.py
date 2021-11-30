def find_median(x):
    x.sort()
    print(x)
    if(len(x)%2==0):
        if(x[len(x)//2]>x[(len(x)//2)-1]):
            return x[len(x)//2]
        else:
            return x[((len(x)//2)-1)]
    else:
        return x[(len(x)//2)]
