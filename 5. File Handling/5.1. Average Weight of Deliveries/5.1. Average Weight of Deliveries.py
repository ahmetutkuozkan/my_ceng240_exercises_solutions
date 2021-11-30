def average_weight(file_name):
    min_value=45
    max_value=125
    average=0
    count_number=0
    with open(file_name,"r") as FILE:
        list1=list(FILE.read().split())
    for i in list1:
        i=int(i)
        if(min_value<=i<=max_value):
            average+=i
            count_number+=1
    if(average!=0):
        return (float(average/count_number))
    else:
        return 0