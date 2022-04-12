from flask import Flask
import random

app = Flask(__name__)
correct_ans = -1



def ans_decorator(func):
    def wrapper_function(*args,**kwargs):
        s = func(int(kwargs['number']))
        if int(kwargs['number'])<correct_ans:
            return "<h1>" + s + "</h1><img src='https://media.giphy.com/media/McKC9Fl4ewe2I/giphy.gif' height=100 width=100></img>"
        elif int(kwargs['number'])>correct_ans:
            return "<h1>" + s + "</h1><img src='https://media.giphy.com/media/iYVneIXJQ3jdJLkZmM/giphy.gif' height=100 width=100></img>"
        else:
            return "<h1>" + s + "</h1><img src='https://media.giphy.com/media/l0Iy1Q9XnpoVP4B8c/giphy.gif' height=100 width=100></img>"
    return wrapper_function

@app.route("/")
def home_route():
    global correct_ans
    correct_ans = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/xxR9sQMGW23EoLsThu/giphy.gif' width=200 height=200></img>"


@app.route("/checkAnswer/<number>")
@ans_decorator
def check_ans(number: int):
    if number==correct_ans:
        return "You found me!"
    elif number<correct_ans:
        return "Too Low!"
    else:
        return "Too High!"


if __name__=='__main__':
    app.run(debug=True)