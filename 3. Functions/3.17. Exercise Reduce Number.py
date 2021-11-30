def helper(y):
    value = 0
    while(True):
        value+=y%10
        if(y>=10):
            y//=10
        elif(y<10):
            break
    return value
def reduce_number(x):
    result = 0
    deger = x
    while(True):
        result=helper(deger)
        if(result>=10):
            deger=result
        elif(result<10):
            break
    return result
