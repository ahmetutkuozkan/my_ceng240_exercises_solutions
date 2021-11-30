def cheapest_flour(input1,output1):
    a=[]
    b=[]
    with open(input1,"r") as input_file:
        number1=0
        for i in input_file.readlines():
            a.append(i.split())
            b.append(int(a[number1][0])/int(a[number1][1]))
            number1+=1
        b=sorted(b,reverse=True)
    with open(output1,"w") as output_file:
        for i in b:
            output_file.write(str(i)+"\n")
