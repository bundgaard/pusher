from flask import Flask, request, render_template
app = Flask(__name__)
app.secret_key = 'D\xea\xcb9h\x02\xb6\x8e\x90\xeb\xa4\rk\xbf\x960\x0bn\xa8\xff;\xac\xadK'

@app.route('/upload', methods=["POST","GET"])
def upload():
	if request.method == "POST":
		return "Please do something POSTable"
	else:
		return "Hi welcome to upload form"
@app.route('/')
@app.route('/<name>')
def index(name=None):
	app.logger.info('index saying hi')
	return render_template('index.html', name=name)
