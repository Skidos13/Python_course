from flask import Flask

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


def create_blog_post(user):
    print (f"This is {user.name}'s new blog post.")

new_user = User("Angela")
create_blog_post(new_user)

# Decorators
def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper
def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/')
@make_emphasis
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<b>Goodbye!</b>'

def greet(name):
    return f'Hello, {name}!'

@app.route('/greet/<name>')
def greet_you(name):
    return greet(name)




if __name__ == '__main__':
    app.run(debug=True)

