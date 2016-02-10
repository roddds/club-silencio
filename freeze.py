#! /usr/bin/env python
from flask_frozen import Freezer
from main import app

app.config['FREEZER_BASE_URL'] = 'http://roddds.github.io/club-silencio/'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()