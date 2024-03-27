import flask 
from dotenv import load_dotenv
load_dotenv()


app=flask.Flask(__name__)

@app.route('/')

def index():
    return 'Hello World'

index()


if __name__ == '__main__':
    app.run(debug=True)