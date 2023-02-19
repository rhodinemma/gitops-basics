from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'The goal is to be next level!!!!'
