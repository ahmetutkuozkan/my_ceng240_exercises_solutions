def format_for_migration(input1,output1):
    with open(input1,"r") as input_file:
        a=[]
        result=[]
        for i in input_file.readlines():
            a.append(i.split(","))
    with open(output1,"w") as output_file:
        for i in range(1,len(a)):
            temp=a[0][0]+":"+a[i][0]+","+a[0][1]+":"+a[i][1]+","+a[0][2].rstrip("\n")+":"+a[i][2].rstrip("\n")
            output_file.write(temp)
            if(i!=27):
                output_file.write("\n")
            result.append(temp)
    return len(a)-1