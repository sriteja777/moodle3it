from flask import Flask

#create the application.
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style=color:blue>This is an index page</h1>"

@app.route('/welcome/')
@app.route('/welcome/<int:id>')
def welcome(id = None):
    if id is None:
        return "<h2 style=color:green>Hello %s !</h2>" % "Unknown User"
    else:
        return "<h2 style=color:green>Hello user%d !</h2>" % id


if __name__ == '__main__':
    app.debug = True
    app.run()
