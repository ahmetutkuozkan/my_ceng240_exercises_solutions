n = int(input())
a=[[0]*n]*n
for i in range(0,n):
    a[i]=input()
b=0
finish=0
for i in range(0,n+1):
    if(a[i][i] == a[i+1][i+1]):
        b+=1
        if(b==3):
            print("yes")
            finish=1
            break
    if(finish==1):
        break
    if(a[i][i] != a[i+1][i+1]):
        break
b=0
for z in range(n+1,0,-1):
    if(a[i][i] == a[i-1][i-1]):
        b+=1
        if(b==3):
            print("yes")
            finish=1
            break
    if(finish==1):
        break
    if(a[i][i] != a[i-1][i-1]):
        break
if(finish==0):
    print("no")