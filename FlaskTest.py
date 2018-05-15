from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello"
    return name

@app.route('/map')
def index():
	return render_template('map.html', title='flask test', message='Hello')

if __name__ == "__main__":
    app.run(debug=True)