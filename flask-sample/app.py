from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        s = func()
        return "<strong>" + s + "</strong>"
    return wrapper_function

def make_emphasis(func):
    def wrapper_function():
        s = func()
        return "<em>" + s + "</em>"
    return wrapper_function

def make_underlined(func):
    def wrapper_function():
        s = func()
        return "<u>" + s + "</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye"


if __name__=="__main__":
    app.run(debug=True)