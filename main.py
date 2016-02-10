#! /usr/bin/env python3
import os
from flask import Flask, send_from_directory
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8001, processes=5)
