def divisors_controller(number):
    a=0
    for i in range(1,(number//2)+1):
        if number%i==0:
            a+=i
    return a
def is_perfect(x):
    if(divisors_controller(x)==x):
        return True
    else:
        return False