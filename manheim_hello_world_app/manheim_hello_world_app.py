# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)