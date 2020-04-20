from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    """ Create form for Login page
    Allow to set reference names for triggers and check validaties for inputs.
    
    Parameters:
    FlaskForm: make sure reference names are matching
    
    4/19 Ali
    
    """
 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
