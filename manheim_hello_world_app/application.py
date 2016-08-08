# -*- coding: utf-8 -*-
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def helloworld():
    return render_template('hello.html')

if __name__ == '__main__':
    application.run('0.0.0.0', port=80, debug=True)