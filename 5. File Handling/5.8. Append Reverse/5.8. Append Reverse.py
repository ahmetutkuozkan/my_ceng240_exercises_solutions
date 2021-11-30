def append_reverse(input1):
    a=[]
    b=[]
    splitted_a=[]
    with open(input1,"r") as input_file:
        for i in input_file.readlines():
            a.append(i)
            splitted_a.append(i.split())

        for i in splitted_a:
            temp=i[1]+" "+i[0]
            b.append(temp)
    with open(input1,"a") as output_file:
        for i in b:
            output_file.write(i+"\n")
    return splitted_a
