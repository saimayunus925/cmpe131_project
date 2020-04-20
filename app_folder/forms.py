from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
    Creating create account fields
    Isaac 4/19: Creates text fields and a submit button on create-account page

'''
class Registerform(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	username = StringField('Set Username', validators=[DataRequired()])
	password = PasswordField('Set Password', validators=[DataRequired()])
	submit = SubmitField('Create Account')