from flask import Flask, url_for, redirect, abort

#create the application.
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style=color:blue>This is an index page</h1>"

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name = None):
    if name is None:
        return "<h2 style=color:green>Hello %s !</h2>" % "Unknown User"
    else:
        return "<h2 style=color:green>Hello %s !</h2>" % name

@app.errorhandler(404)
def page_error(error):
    return '<h2/>Sorry! resource you want to access is not there.<br>:-(<br> error=%s'%error

@app.route('/show_account/')
def show_account():
    logged_in = False
    if not logged_in:
        abort(401)
    return "balance is ..."

if __name__ == '__main__':
    app.debug = True
    app.run()
