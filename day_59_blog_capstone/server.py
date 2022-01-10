from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/8d2d25d2afea89316a52'
    response = requests.get(blog_url)
    all_blog_posts = response.json()
    return render_template('index.html', posts=all_blog_posts)

@app.route('/blogpost/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/8d2d25d2afea89316a52'
    response = requests.get(blog_url)
    all_blog_posts = response.json()
    return render_template('post.html', posts=all_blog_posts, post_id=int(num))

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')




if __name__ == "__main__":
    app.run(debug=True)
