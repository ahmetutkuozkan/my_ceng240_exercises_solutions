def mygcdfunction(x, y):
    z=(x%y)
    if(z==0):
        if(x>y):
            z=y
        else:
            z=x
    return z
x = int(input()); y = int(input()); print(int(mygcdfunction(x,y)))