import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {self.current_question.text}"
        # user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False):')
        # self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False


