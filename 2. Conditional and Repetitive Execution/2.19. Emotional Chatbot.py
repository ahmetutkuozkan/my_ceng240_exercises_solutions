text = list(input())
control=0
for i in range(len(text)):
    if(i%2==0 and text[i]=="u"):
        control+=1
    elif(text[i]=="h"):
        control+=1
if(control==len(text)):
    print("Are you sad, hooman?")
else:
    print("I am so sad, hooman.")