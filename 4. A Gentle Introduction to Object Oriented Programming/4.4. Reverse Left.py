def reverse_left(list1,x):
    a=0
    for i in range(len(list1)):
        if(x==list1[i]):
            a=i
            break
    b=list1[:a]
    new_list=b[-1::-1]+list1[a:]
    return new_list
