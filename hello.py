from flask import Flask

app = Flask(__name__)

# 使用装饰器的路由解析URL
@app.route('/')
def index():
	return '<h1> Hello World!</h1>'
	
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello, %s!</h1>'% name

# host='0.0.0.0' 可以外网访问
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)