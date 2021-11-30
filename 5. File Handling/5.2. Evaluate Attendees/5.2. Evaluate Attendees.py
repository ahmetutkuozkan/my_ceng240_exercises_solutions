def evaluate_attendees(key,grade):
    GRADES=[]
    NAMES_and_GRADES=[]
    with open(key,"r") as key_file:
        KEY1=key_file.read().split()
    with open(grade,"r") as grade_file:
        lines1=grade_file.readlines()
        GRADES=[0]*len(lines1)
        aa=0
        for i in lines1:
            true1=0
            false1=0
            GRADES[aa]=i.split()
            aaa=0
            for i in GRADES[aa][1:]:
                if(i==KEY1[aaa]):
                    true1+=1
                else:
                    false1+=1
                aaa+=1
            NAMES_and_GRADES.append((GRADES[aa][0],true1-0.25*false1))
            aa+=1
        result=sorted(NAMES_and_GRADES, key=lambda item: item[1], reverse=True)
        return result
