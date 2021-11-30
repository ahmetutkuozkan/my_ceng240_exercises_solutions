def sampled_average(x,y):
    result=sum(x)-y*(len(x)-1)
    b= result in x
    if(b==0):
        return 'no'
    else:
        return 'yes'


