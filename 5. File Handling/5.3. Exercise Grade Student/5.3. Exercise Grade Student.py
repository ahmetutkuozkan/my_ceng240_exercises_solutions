def grade_student(answer_key,student_answer):
    Answers=[]
    Student_Answers=[]
    result=0
    a_count=0
    with open(answer_key,"r") as answer_file:
        a=answer_file.readlines()
        a_count=len(a)
        for i in a:
            Answers.append(i.split())
    with open(student_answer,"r") as student_file:
        a=student_file.readlines()
        for i in a:
            Student_Answers.append(i.split())
    for i in range(a_count):
        if(Answers[i][1]==Student_Answers[i][1]):
            result+=int(Answers[i][2])
    print(result)
