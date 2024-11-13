from flask import Flask 

app = flask("flaskapp")

app.route('/', methods = ['GET'])
def welcome():
    return "<h1> Hello world </h2>"
    
if __name__ = "__main__":
    app.run()