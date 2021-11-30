wanted_width = int(input()); height_b = int(input()); width_b = int(input())
a=wanted_width%height_b
exitvalue=0
while(exitvalue==0):
    if(a%width_b!=0):
        a+=height_b
        if(a%width_b==0):
            print("YES")
            exitvalue=1
        elif(a>wanted_width):
            print("NO")
            exitvalue=1


