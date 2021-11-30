people_age = eval(input())
total_ticket_price = 0
for i in people_age:
    if (0 <= i <= 10):
        total_ticket_price += 30
    elif(11 <= i <= 25):
        total_ticket_price += 60
    elif(26 <= i <= 60):
        total_ticket_price += 90
    elif(60 < i):
        total_ticket_price += 50
print(total_ticket_price)


