from app import app
from flask import render_template
import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', title='about', form=form)