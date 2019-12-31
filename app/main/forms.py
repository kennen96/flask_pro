from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TtForm(FlaskForm):
    ttt1 = RadioField('method', choices=[(1, 'GET'), (2, 'POST')], default = 1)
    ttt2 = RadioField('method', choices=[(1, 'GET'), (2, 'POST')], default = 1)
    submit = SubmitField('Submit')