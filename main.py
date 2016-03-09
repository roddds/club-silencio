#! /usr/bin/env python3
import os
from flask import Flask, send_from_directory
from flask import render_template, request
from flask.ext.babelex import Babel


app = Flask(__name__)
app.debug = True

babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def selector(language_code=None):
    if not language_code or language_code not in ('en', 'pt'):
        language_code = 'en'

    if language_code == 'pt':
        language_code = 'pt_BR'

    def get_locale():
        return language_code

    babel.locale_selector_func = get_locale


@app.route('/')
@app.route('/<lang>/')
def home(lang=None):
    selector(lang)
    return render_template('home.html', lang=lang)


@app.route('/about/')
@app.route('/about/<lang>/')
def about(lang=None):
    selector(lang)
    return render_template('about.html', lang=lang)


@app.route('/music/')
@app.route('/music/<lang>/')
def music(lang=None):
    selector(lang)

    context = {
        'STATIC_URL': app.static_url_path,
    }
    return render_template('music.html', lang=lang, **context)


@app.route('/contact/')
@app.route('/contact/<lang>/')
def contact(lang=None):
    selector(lang)
    return render_template('contact.html', lang=lang)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8001, processes=5)
