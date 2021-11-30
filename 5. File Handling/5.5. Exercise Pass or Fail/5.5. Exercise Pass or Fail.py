def pass_or_fail(input1,output1):
    a=[]
    temp=[]
    temp2=[]
    person=[]
    temp1=[]
    aa=0
    with open(input1,"r") as input_file:
        for i in input_file.readlines():
            a.append(i.split())
            temp2=a[aa][1].split(",")
            temp1=[a[aa][0]]
            temp3=temp1+temp2
            temp.append(temp3)
            aa+=1
    with open(output1,"w") as output_file:

        for i in range(len(temp)):
            if((int(temp[i][2])*0.30 + int(temp[i][3])*0.30 + int(temp[i][4])*0.40)>=60):
                output_file.write(temp[i][0]+" "+temp[i][1]+",Pass\n")
            else:
                output_file.write(temp[i][0]+" "+temp[i][1]+",Fail\n")
