Tuble1 = eval(input()); Tuble2 = eval(input())
array1 = [0]*10000
array2 = [0]*10000

x=0
for i in Tuble1:
    array1[x] = i
    x+=1
aa = x
x=0
for i in Tuble2:
    array2[x] = i
    x+=1
array1[array2[0]]=array2[1]
print("(",end="")
for z in range(aa):
    if(z!=0):
        print(end=",")
    print(array1[z],end="")
print(")",end="")
