from flask import Flask

#create the application.
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style=color:blue>This is an index page</h1>"

@app.route('/welcome')
def welcome():
    return "<h2 style=color:green>This is a greeting page.</h2>"


if __name__ == '__main__':
    app.debug = True
    app.run()
