from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        return user_answer == self.answer


from datetime import datetime

class CBT:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.history = []

    def add_question(self, question):
        self.questions.append(question)

    def answer_question(self, question, user_answer):
        if question.is_correct(user_answer):
            self.score += 1

        self.history.append((question.text, user_answer))

    def get_result(self):
        percentage = (self.score / len(self.questions)) * 100

        return {
            "score": self.score,
            "total": len(self.questions),
            "percentage": percentage,
            "time": datetime.now()
        }