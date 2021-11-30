from math import *
r1_x = int(input()); r1_y = int(input()); r1_r = int(input())
r2_x = int(input()); r2_y = int(input()); r2_r = int(input())
length = sqrt(pow(r1_x-r2_x,2)+pow(r1_y-r2_y,2))-r1_r-r2_r
print("%.2f" % length)