from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def receive_data():
	username = request.form.get('username')
	password = request.form.get('password')
	if request.method == 'POST':
		return f"<h1>Name: {username}, Password: {password}</h1>"
	else:
		render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

