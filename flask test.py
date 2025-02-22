# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:24:37 2025

@author: user
"""

# app.py

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Replace with your script logic
        result = subprocess.check_output(['python', 'your_script.py'], text=True)
        return jsonify({"status": "success", "output": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run()