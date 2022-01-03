from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def say_hello():
    random_number = random.randint(0, 11)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<your_name>')
def guesser(your_name):
    # getting the age of user
    agify_api = requests.get(f'https://api.agify.io?name={your_name}')
    agify_data = agify_api.json()
    user_age = agify_data['age']

    # getting the gender of user
    genderize_api = requests.get(f'https://api.genderize.io/?name={your_name}')
    genderize_data = genderize_api.json()
    user_gender = genderize_data["gender"]

    return render_template("user.html", name=your_name.capitalize(), age=user_age, gender=user_gender)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_blog_posts = response.json()
    print(num)
    return render_template("blog.html", posts=all_blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
