from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Goodbye!'

def greet(name):
    return f'Hello, {name}!'

@app.route('/greet/<name>')
def greet_you(name):
    return greet(name)

if __name__ == '__main__':
    app.run(debug=True)