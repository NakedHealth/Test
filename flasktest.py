# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:24:37 2025

@author: user
"""

# app.py

from flask import Flask, jsonify
from flask_cors import CORS

import subprocess


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()