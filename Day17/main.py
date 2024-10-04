from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
question_bank=[]
for i in question_data:
    new_question=Question(i["text"],i["answer"])
    question_bank.append(new_question)
quiz=Quiz_brain(question_bank)
quiz.show_question(question_number=quiz.question_number,question_list=quiz.question_list)