def reinstall(x):
    y = dict()
    y_last=dict()
    a=0
    z=""
    z_number=""
    for i in x:
        if(i=='|'):
            a=1
        elif(i==':'):
            a=2
        elif(i=='='):
            a=0
        elif(i!=' ' and a==1):
            z+=i
        elif(i!=' ' and a==2):
            z_number+=i
        elif(i==' ' and a==2 and z_number!=""):
            y[z[0].upper()+z[1:].lower()]=int(z_number)
            z=""
            z_number=""
    ii=0
    list1=[0]*len(y.keys())
    for i in y.keys():
        list1[ii]=ord(i[0])
        ii+=1
    list_name=[0]*len(y.keys())
    list_age=[0]*len(y.keys())
    ii=0
    for i in y.keys():
        list_name[ii]=i
        ii+=1
    ii=0
    for j in y.values():
        list_age[ii]=j
        ii+=1

    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if(list1[i]==list1[j]):
                list1[i]-=1

    list1_sorted=sorted(list1)
    for i in list1_sorted:
        for j in range(len(list1)):
            if(i==list1[j]):
                zz={str(list_name[j]): int(list_age[j])}
                y_last.update(zz)
    return y_last