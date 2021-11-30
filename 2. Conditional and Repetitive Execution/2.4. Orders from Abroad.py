count_of_items=int(input())
total_tax = 0
for i in range(0,count_of_items):
    price=int(input())
    if(100 < price <=1000):
        total_tax+=price*0.1
    elif(1000 < price):
        total_tax+=price*0.2

print(float(total_tax))