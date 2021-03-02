from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import *


class LoginForm(FlaskForm):
    ans1 = IntegerField('2 + 2 * 2')
    ans2 = IntegerField('77 + 33')
    submit = SubmitField('Войти')