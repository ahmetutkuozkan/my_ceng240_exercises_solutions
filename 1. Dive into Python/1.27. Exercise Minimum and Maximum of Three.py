from math import *
val1 = int(input()); val2 = int(input()); val3 = int(input())
deger1 = min(val1,val2,val3)
deger3 = max(val1,val2,val3)
deger2 =val1+val2+val3-deger1-deger3
print(str(deger1)+" "+str(deger2)+" "+str(deger3))
