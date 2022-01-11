from flask import Flask, request, render_template
import requests
import smtplib

local_email = 'nyelrugosibakugan@gmail.com'
local_password = 'xxxx'

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
def get_contact_page():
    return render_template('contact.html')


@app.route('/contact/done', methods=['GET', 'POST'])
def get_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=local_email, password=local_password)
        connection.sendmail(
            from_addr=local_email,
            to_addrs=email,
            msg=f"Subject:New Message\n\nContact name: {name}\nContact email: {email}\nContact phone: {phone}\nContact message: {message}")
    return render_template('contact.html')




if __name__ == "__main__":
    app.run(debug=True)
