from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center;'>Hello, World!</h1>" \
           "<p>image below</p>" \
           "<img src='https://media1.giphy.com/media/3o7aDfk8UmiioXaeoo/giphy.gif?cid" \
           "=ecf05e47awmskon29oackpe30vf2b4emvvz0uyuqb05i0u5m&rid=giphy.gif&ct=g'> "


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


@app.route("/bye")
@make_bold
def bye():
    return "bye"


@app.route('/<name>/<int:number>')
def greeting(name, number):
    return f"O hi there {name + '2'}, you are {number}!"


if __name__ == "__main__":
    app.run(debug=True)
