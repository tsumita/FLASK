from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/index')
def index():
	return render_template('index.html', title='flask test', message='Hello')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)