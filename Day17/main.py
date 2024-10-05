from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
question_bank=[]
for i in question_data:
    new_question=Question(i["text"],i["answer"])
    question_bank.append(new_question)
quiz=QuizBrain(question_bank)
quiz.show_question(question_list=quiz.question_list)