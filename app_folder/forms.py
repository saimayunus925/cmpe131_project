from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Email, Required
from app_folder import funcs
import datetime
 
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
    delete = SubmitField('Delete Account')
    submit = SubmitField('Submit')
    timeops = SelectField('Length of Meeting', choices=[(15, '15 minutes'), (30, '30 minutes'), (60, '60 minutes')])
    #timeofday = SelectField('Time of Meeting', choices=[('1', '9:00am'), ('2', '10:00am'), ('3', '11:00am'), ('4', '12:00pm'), ('5', '1:00pm'), ('6', '2:00pm'), ('7', '3:00pm'), ('8', '4:00pm'), ('9', '5:00pm'), ('10', '6:00pm'), ('11', '7:00pm'), ('12', '8:00pm'), ('13', '9:00pm'), ('14', '10:00pm')])
    
    times=[]
    for x in range(9, 23):
        dt = datetime.time(x, 00)
        times.append((x, dt.strftime('%I:%M %p')))


    start_time_of_day = SelectField('Start Time:  ', choices=times)
    end_time_of_day = SelectField('End Time:  ', choices=times)


class DeleteForm(FlaskForm):
    #email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Confirm Username', validators=[DataRequired()])
    password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Delete Account')

class ScheduleMeetingForm(FlaskForm):
    '''
    Calendar selecter for guest

    Changelog:
        5/10 Dylan: Initial implementation
    '''
    date = DateField('Meeting date', validators=[Required()], default='')
    submit = SubmitField('Check times')

class MeetingDescriptionForm(FlaskForm):
    '''
    Inputs when a guest schedules a meeting


    Changelog:
        5/11 Dylan: Initial implementation
    '''
    time = SelectField('Time', choices = [])
    name = StringField('Your name', validators=[DataRequired()])
    description = TextAreaField('Meeting Description (optional)')
    submit = SubmitField('Schedule')