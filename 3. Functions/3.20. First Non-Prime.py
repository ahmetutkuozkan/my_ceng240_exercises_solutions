def prime_controller(y):
    for i in range(2,(y//2)+1):
        if y%i==0:
            return False
    return True
def find_first_non_prime(x):
    for i in range(len(x)):
        if 0==prime_controller(x[i]):
            return x[i]
    return False