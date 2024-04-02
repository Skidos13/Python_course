from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    #path will be from \tempates folder
    return render_template(r"/index.html")




#this makes the app run on the server constantly
if __name__ == '__main__':
    app.run(debug=True)