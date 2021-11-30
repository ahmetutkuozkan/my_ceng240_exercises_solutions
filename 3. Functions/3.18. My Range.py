def my_range(first,last,increase):
    if(first>last):
        return []
    else:
        return [first]+my_range(first+increase,last,increase)