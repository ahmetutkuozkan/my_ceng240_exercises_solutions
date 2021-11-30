value1 = int(input()); value2 = value1//100
if value1 % 2==0 and value2 % 2==0:
    print("Even")
elif value1 % 2==0 and value2 % 2==1:
    print("Even Odd")
elif value1 % 2==1 and value2 % 2==1:
    print("Odd")
elif value1 % 2==1 and value2 % 2==0:
    print("Odd Even")
