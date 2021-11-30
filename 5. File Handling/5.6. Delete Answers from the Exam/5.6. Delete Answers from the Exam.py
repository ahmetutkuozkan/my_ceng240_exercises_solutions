def delete_answers(questions):
    Questions=[]
    with open(questions,"r") as questions_file:
        for i in questions_file.readlines():
            Questions.append(i)
    Questions_index=len(Questions)
    with open("new_questions.txt","w") as new_question_file:
        for i in range(Questions_index):
            if((i+1)%6!=0):
                new_question_file.write(Questions[i])
