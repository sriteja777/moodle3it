from flask import Flask, url_for

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

@app.route('/test1/')
def test1():
    fname = 'welcome'
    return "url for function %s=<h1/>%s" % (fname, url_for(fname))

@app.route('/test2/')
def test2():
    fname, name = 'welcome', 'foo'
    return "url for function= %s with name= %s is <h1/> %s" % (fname,name,url_for(fname, name = name))


if __name__ == '__main__':
    app.debug = True
    app.run()
