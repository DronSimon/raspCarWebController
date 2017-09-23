from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='', static_url_path='')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/a')
def a():
	print('a')
	return 'a2'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
