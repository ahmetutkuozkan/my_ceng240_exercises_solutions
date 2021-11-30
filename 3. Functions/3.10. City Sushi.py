def total_price(x,y,z):
    result=0
    for i in range(y-1,z-1):
        result+=x[i]
    return result
