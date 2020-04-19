from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Set Username', validators=[DataRequired()])
    password = PasswordField('Set Password', validators=[DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Sign On')

class createAccountForm(FlaskForm):
    username = StringField('Set Username', validators=[DataRequired()])
    password = PasswordField('Set Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    confirm_email = StringField('Confirm Email', validators=[DataRequired()])
    submitCA = SubmitField('Submit To Create Account')

class LogOutForm(FlaskForm):
    signOut = SubmitField('Sign-Out')

