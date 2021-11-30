def sum_prices(shopping_list):

    total = 0
    for (item, price) in shopping_list:
        total += price

    return round(total, 2)

def calculate_expenses(list1):
    calculated=[]
    for part_of_list in list1:
        try:
            calculated.append(sum_prices(part_of_list))
        except:
            calculated.append("Incomplete")
    return calculated
