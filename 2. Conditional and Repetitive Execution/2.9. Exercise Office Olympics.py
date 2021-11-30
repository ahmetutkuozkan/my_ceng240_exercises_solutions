#wins_list = [("jim", 11), ("pam", 9), ("dwight", 12), ("oscar", 2), ("micheal", 17), ("angela", 3), ("kevin", 1)]
#["micheal", "dwight", "jim"]
wins_list = [("jim", 1), ("pam", 4), ("jan", 10), ("creed", 7), ("micheal", 5), ("meredith", 2), ("phyllis", 28)]
# #["phyllis", "jan", "creed"]
a = 0
b = 0

c = [0]*len(wins_list)
z = [0]*3
for i in range(len(wins_list)):
    #print(wins_list[i][1])
    a=wins_list[i][1]
    c[i]=a


c=sorted(c,reverse=True)
aa = [0]*3
for i in range(0,3):
    aa[i]=c[i]
for y in range(0,3):
    for b in range(0,len(wins_list)):
        if(wins_list[b][1]==aa[y]):
            z[y]=wins_list[b][0]
            break
print(z)


