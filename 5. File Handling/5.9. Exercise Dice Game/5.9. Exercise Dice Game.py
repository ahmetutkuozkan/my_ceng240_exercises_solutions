def dice_game(input1):
    a=[]
    player1=0
    player2=0
    player3=0
    winner=""
    with open(input1,"r") as input_file:
        for i in input_file.readlines():
            a.append(i.split())
        name=[]
        name=a[0]

    for i in a[1:]:
        i[0]=int(i[0]);i[1]=int(i[1]);i[2]=int(i[2])
        if(i[0]==i[1]==i[2]):
            player1+=0.33;player2+=0.33;player3+=0.33
        elif(i[0]==i[1]):
            if(i[0]>i[2]):
                player1+=0.5;player2+=0.5
            else:
                player3+=1
        elif(i[1]==i[2]):
            if(i[1]>i[0]):
                player2+=0.5;player3+=0.5
            else:
                player1+=1
        elif(i[0]==i[2]):
            if(i[0]>i[1]):
                player1+=0.5;player3+=0.5
            else:
                player2+=1
        elif(i[0]!=i[1]!=i[2]):
            if(i[0]>i[1]):
                if(i[0]>i[2]):
                    player1+=1
                elif(i[2]>i[0]):
                    player3+=1
            elif(i[1]>i[0]):
                if(i[1]>i[2]):
                    player2+=1
                elif(i[2]>i[1]):
                    player3+=1
            elif(i[2]>i[1]):
                if(i[2]>i[0]):
                    player3+=1
                elif(i[0]>i[2]):
                    player1+=1

    if(player3==player2==player1):
        winner=name[0]+","+name[1]+","+name[2]+" "+str(player1)
    elif(player2==player1):
        winner=name[0]+","+name[1]+" "+str(player1)
    elif(player3==player1):
        winner=name[0]+","+name[2]+" "+str(player1)
    elif(player3==player2):
        winner=name[1]+","+name[2]+" "+str(player2)
    elif(player1>player2):
        if(player1>player3):
            winner=name[0]+" "+str(player1)
        else:
            winner=name[2]+" "+str(player3)
    elif(player2>player1):
        if(player2>player3):
            winner=name[1]+" "+str(player2)
        else:
            winner=name[2]+" "+str(player3)
    elif(player3>player1):
        if(player3>player2):
            winner=name[2]+" "+str(player3)
        else:
            winner=name[1]+" "+str(player2)
    return winner
