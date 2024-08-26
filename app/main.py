import sys
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)