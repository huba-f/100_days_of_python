from flask import Flask, request, render_template, redirect
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def front_page_gif():
    return render_template("home-page.html")


@app.route(f'/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if int(text) > random_number:
        return render_template("too_high.html")
    elif int(text) < random_number:
        return render_template("too-low.html")
    else:
        return render_template("won.html")


if __name__ == "__main__":
    app.run(debug=True)
