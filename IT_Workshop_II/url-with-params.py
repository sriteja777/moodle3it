from flask import Flask

#create the application.
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style=color:red>This is an index page</h1>"

@app.route('/welcome/<name>')
def welcome(name=None):
    return "<h2 style=color:green>Hello %s !</h2>"%name

if __name__ == '__main__':
    app.debug = True
    app.run()
