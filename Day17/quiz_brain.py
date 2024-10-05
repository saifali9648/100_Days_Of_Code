class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list
        self.negative_score=0
    def show_question(self,question_list):
        for current_question in question_list:
            user_answer=input(f"Q{self.question_number+1}: {current_question.question} True/False: ")
            if user_answer==current_question.correct_answer:
                print(current_question.correct_answer)
                self.question_number+=1
                self.score+=1
                print(f"your score is {self.score}")
            else:
                self.question_number+=1
                print(f"you answer is wrong and your score is {self.score}")
                print(current_question.correct_answer)
        print(f"your final score is {self.score}")

