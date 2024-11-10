from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions
questions = [
    {
        "question": "What is the correct syntax to output 'Hello, World' in Python?",
        "options": ["A) echo('Hello, World')", "B) p('Hello, World')", 
                    "C) print('Hello, World')", "D) printf('Hello, World')"],
        "answer": "C"
    },
    {
        "question": "Which of the following data types is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
        "answer": "D"
    },
    {
        "question": "What will `5 ** 3` return in Python?",
        "options": ["A) 15", "B) 125", "C) 8", "D) Error"],
        "answer": "B"
    },
    {
        "question": "What is the result of `len('Python')`?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B"
    },
    {
        "question": "How do you create a list in Python?",
        "options": ["A) list = {}", "B) list = []", "C) list = ()", "D) list = <>"],
        "answer": "B"
    },
    {
        "question": "What is the output of `type([])` in Python?",
        "options": ["A) <class 'list'>", "B) <class 'tuple'>", 
                    "C) <class 'dict'>", "D) <class 'set'>"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "What will `print(2 == 2.0)` output?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "A"
    },
    {
        "question": "Which operator is used to multiply numbers in Python?",
        "options": ["A) x", "B) *", "C) /", "D) %"],
        "answer": "B"
    },
    {
        "question": "What is the result of `bool('')` in Python?",
        "options": ["A) True", "B) False", "C) 0", "D) None"],
        "answer": "B"
    }
]

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for question in questions:
        selected_answer = request.form.get(question['question'])
        if selected_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
