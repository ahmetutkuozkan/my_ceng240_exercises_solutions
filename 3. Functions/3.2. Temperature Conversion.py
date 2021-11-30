def convert(x,y):
    if y=="C":
        return round(180*(x/100)+32,2)
    elif y=="F":
        return round(100*((x-32)/180),2)
    else:
        return "inavlid unit"
