from flask import Flask

#create the application.
app = Flask(__name__)

@app.route('/')
def helloworld():
    """ Displays hello world string at '/'"""
    return "<h1 style=color:blue>Hello World</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run()
