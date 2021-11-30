def readable(list1):
    splitted_list=list1.split(",")
    for i in splitted_list:
        for j in i:
            if(j!=" "):
                print(j.lower(),end="")
        print("")
