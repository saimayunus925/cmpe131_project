from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    """ Create form for Login page
    Allow to set reference names for triggers and check validaties for inputs.
    Summary for things we need for inside Login page
    
    Parameters:
        FlaskForm: make sure reference names are matching
    
    Changelog:
        4/19 Ali
    
    """
 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    '''
    Creating create account fields

    Changelog:
        Isaac 4/19: Creates text fields and a submit button on create-account page
    '''
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Set Username', validators=[DataRequired()])
    password = PasswordField('Set Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')
