from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField
from wtforms.validators import (DataRequired, Regexp, ValidationError)
import datetime
from models import Entry

class EntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()])
    date = DateField(
        'Date Created',
        validators=[DataRequired()],

    )
    timeSpent = StringField(
        'Time Spent',
        validators=[DataRequired()]
    )
    whatILearned = TextAreaField('What I Learned', validators=[DataRequired()])
    ResourcesToRemember = TextAreaField('Resources to Remember', validators=[DataRequired()])

