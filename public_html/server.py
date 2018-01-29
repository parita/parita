# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:20:34 2016

@author: Rohan Kulkarni
@email : rohan.kulkarni@columbia.edu

"""

from __future__ import print_function
import sys

from flask import Flask,render_template
import math
from urllib import urlopen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/projects/gsoc-2013/')
def gsoc():
    return render_template('gsoc-2013.html')

@app.route('/teaching/')
def teaching():
    return render_template('teaching.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=8078)
