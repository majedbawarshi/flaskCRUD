from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# for form validation
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
