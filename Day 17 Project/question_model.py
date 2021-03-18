question_model.py

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        

        
data.py

question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "The programming language 'Python' is based off a modified version of 'JavaScript'.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "RAM stands for Random Access Memory.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "Ada Lovelace is often considered the first computer programmer.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "The Windows ME operating system was released in the year 2000.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linux was first created as an alternative to Windows XP.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    }, 
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question":
        "The Python programming language gets its name from the British comedy group 'Monty Python.'",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }
]
