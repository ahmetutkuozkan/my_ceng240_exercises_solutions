def find_zero(x):
    index1=0
    index1_zero=-1
    for number in x:
        try:
            1000/number
            index1+=1
        except ZeroDivisionError:
            index1_zero=index1
            return index1_zero
    return index1_zero
