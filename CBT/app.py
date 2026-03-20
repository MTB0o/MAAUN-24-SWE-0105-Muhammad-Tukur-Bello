from flask import Flask, render_template, request
from models import Question, CBT

app = Flask(__name__)

# Create CBT object
cbt = CBT()

# Add questions (VERY IMPORTANT)
cbt.add_question(Question(
    "What is 2 + 2?",
    ["2", "3", "4", "5"],
    "4"
))

cbt.add_question(Question(
    "Capital of Nigeria?",
    ["Lagos", "Abuja", "Kano", "Ibadan"],
    "Abuja"
))

cbt.add_question(Question(
    "What is 5 * 6?",
    ["11", "30", "56", "25"],
    "30"
))

cbt.add_question(Question(
    "Which language is used for web apps?",
    ["Python", "HTML", "Java", "All of the above"],
    "All of the above"
))

cbt.add_question(Question(
    "What does CPU stand for?",
    ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit"],
    "Central Processing Unit"
))

cbt.add_question(Question(
    "Which of these is a Python data type?",
    ["List", "String", "Dictionary", "All of the above"],
    "All of the above"
))

cbt.add_question(Question(
    "What is the capital of France?",
    ["Berlin", "Madrid", "Paris", "Rome"],
    "Paris"
))

cbt.add_question(Question(
    "Which symbol is used for comments in Python?",
    ["//", "#", "/* */", "--"],
    "#"
))

cbt.add_question(Question(
    "What is 10 / 2?",
    ["2", "3", "5", "10"],
    "5"
))

cbt.add_question(Question(
    "Which keyword is used to create a function in Python?",
    ["fun", "define", "def", "function"],
    "def"
))

cbt.add_question(Question(
    "What is the largest planet in our solar system?",
    ["Earth", "Jupiter", "Mars", "Saturn"],
    "Jupiter"
))

cbt.add_question(Question(
    "Which collection is ordered, changeable, and allows duplicate members?",
    ["Set", "Dictionary", "Tuple", "List"],
    "List"
))

cbt.add_question(Question(
    "Which country is known as the Giant of Africa?",
    ["Ghana", "Nigeria", "Kenya", "South Africa"],
    "Nigeria"
))

cbt.add_question(Question(
    "Which data structure uses FIFO?",
    ["Stack", "Queue", "Array", "Tree"],
    "Queue"
))

# Home route (shows questions)
@app.route('/')
def home():
    print("Questions:", cbt.questions)  # debug line
    return render_template("index.html", questions=cbt.questions)


# Submit route (process answers)
@app.route('/submit', methods=['POST'])
def submit():
    # Reset score before new attempt
    cbt.score = 0
    cbt.history = []

    for i, question in enumerate(cbt.questions):
        user_answer = request.form.get(question.text)
        cbt.answer_question(question, user_answer)

    result = cbt.get_result()
    return render_template("result.html", result=result)


# Run app
if __name__ == '__main__':
    app.run(debug=True)