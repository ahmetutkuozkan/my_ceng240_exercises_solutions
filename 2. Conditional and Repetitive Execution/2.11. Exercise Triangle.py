from math import *
x = int(input()); y = int(input()); z = int(input())
if(abs(z-y)<x<z+y):
    if(abs(z-x)<y<z+x):
        if(abs(y-x)<z<y+x):
                print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")