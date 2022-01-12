from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import validators

ADMIN_EMAIL = "admin@mail.com"
ADMIN_PASSWORD = "12345678"


app = Flask(__name__)

app.config["SECRET_KEY"] = "intel"
# create Form Class
class LoginForm(FlaskForm):
    name = StringField("what is you name", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("what is your password", validators=[validators.DataRequired(), validators.Length(min=8, max=32)])
    submit = SubmitField("submit")


# create home page
@app.route("/")
def home():
    return render_template('index.html')


# create login page
@app.route("/login", methods=["get", "post"])
def login():
    name = None
    password = None
    form = LoginForm()
    # validate 
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data 
        if name == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            return render_template('authorized.html')
        else:
            return render_template('not_authorized.html')    
        form.name.data = "" 
        form.password.data = ""  
    return render_template('login.html', name=name, password=password, form=form)


if __name__ == '__main__':
    app.run(debug=True)