class Quiz_brain():
    def __init__(self, question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list
        self.negative_score=0
    def show_question(self,question_number,question_list):
        for current_question in question_list:
            user_answer=input(f"Q{self.question_number+1}: {current_question.text} True/false: ").lower()
            self.current_question_anwer=current_question.answer
            if user_answer==self.current_question_anwer:
                print(current_question.answer)
                # current_question=self.question_list[self.question_number]
                # user_aswer=input(f"Q{self.question_number+1}: {current_question.text} True/false: ")
                self.question_number+=1
                self.score+=1
                print(f"your score is {self.score}")
            else:
                self.question_number+=1
                print(f"you answer is wrong and your score is {self.score}")
        print(f"your final score is {self.score}")

