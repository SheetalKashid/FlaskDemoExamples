from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	return "hello world"


@app.route('/hello')
def hello():
	return "hello sheetal!!"


def home():
	return "****My Home!!***"
app.add_url_rule('/home','home',home)


if __name__=="__main__":
	app.run(debug=True)
