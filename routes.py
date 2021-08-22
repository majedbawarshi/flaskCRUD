from app import app
from flask import render_template
import forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# the routes expect the request method to be get by default
@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    # receving the information sended by the form
    if form.validate_on_submit():
        # this message will be printed on the cmd panel when a form is submitted.
        print('Information has been submitted.\nThe data are', form.title.data)
    return render_template('about.html', title='about', form=form)