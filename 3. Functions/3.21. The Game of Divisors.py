def divisors_controller(number):
    a=1
    for i in range(1,(number//2)+1):
        if number%i==0:
            a+=1
    return a
def winner(nazif,osman):
    Nazif=divisors_controller(nazif)
    Osman=divisors_controller(osman)

    if Nazif>Osman:
        return "Nazif"
    elif Osman>Nazif:
        return "Osman"
    else:
        return "Draw"