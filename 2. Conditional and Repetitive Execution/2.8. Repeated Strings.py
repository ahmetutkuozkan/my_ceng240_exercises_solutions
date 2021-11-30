halvable = input()
lentgh = len(halvable)
a = 0
if(lentgh %2==1):
    print("Error")


elif(lentgh%2==0):
    for i in range(0,int(lentgh/2)):
        if(halvable[i]!=halvable[int((lentgh/2)+i)]):
            print("No")
            a=0
            break
        elif(halvable[i]==halvable[int((lentgh/2)+i)]):
            a=1
if(a==1):
    print("Yes")