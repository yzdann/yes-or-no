from flask import render_template
from app import app
from .utils import yes_or_no


@app.route('/')
@app.route('/index')
def index():
    result = yes_or_no()
    return render_template('index.html', result=result)
