def is_time_valid(x):
    if(len(x)>5 or len(x)<5):
        return False
    arr1=x.split(".")
    z=int(arr1[0])
    y=int(arr1[1])
    if(type(z) is int and type(z) is int):
        if(0<=z<24):
            if(0<=y<60):
                return True
            else:
                return False
        else:
            return False
    else:
        return False