def average_discount(list_of_changes):
    total = 0
    count = 0
    for change in list_of_changes:
        if change < 0:
            total += (- change)
            count += 1

    return round((total / count), 2)
def calculate_discount_averages(x):
    result=[]
    for i in x:
        try:
            y=average_discount(i)
        except ZeroDivisionError:
            y=0
        result.append(y)
    return result