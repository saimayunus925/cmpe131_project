from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
 
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
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Set Username', validators=[DataRequired()])
    password = PasswordField('Set Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

class SettingsForm(FlaskForm):
    emailconf = BooleanField('Send Email Confirmation')
    submit = SubmitField('Delete Account')
    confirm = SubmitField('Submit')
    timeops = SelectField('Length of Meeting', choices=[('fifteenmins', '15 minutes'), ('thirtymins', '30 minutes'), ('sixtyymins', '60 minutes')])
    timeofday = SelectField('Time of Meeting', choices=[('1', '9:00am'), ('2', '10:00am'), ('3', '11:00am'), ('4', '12:00pm'), ('5', '1:00pm'), ('6', '2:00pm'), ('7', '3:00pm'), ('8', '4:00pm'), ('9', '5:00pm'), ('10', '6:00pm'), ('11', '7:00pm'), ('12', '8:00pm'), ('13', '9:00pm'), ('14', '10:00pm')])


class DeleteForm(FlaskForm):
    #email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Confirm Username', validators=[DataRequired()])
    password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Delete Account')