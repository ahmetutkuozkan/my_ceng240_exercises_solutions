def fix_operation_file(input1,output1):
    a=[]
    with open(input1,"r") as input_file:
        for i in input_file.readlines():
            a.append(i.rstrip())
        b=[]
        counter1=0

        for i in a:
            if(counter1==0):
                c=str(i)
                counter1+=1
            elif(counter1<=2):
                c+=str(i)
                counter1+=1
            if(counter1==3):
                b.append(c)
                c=""
                counter1-=3
        result=[]
        with open(output1,"w") as output_file:
            for i in b:
                output_file.write(str(i)+"\n")
                result.append(eval(i))
    return result

