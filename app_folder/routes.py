from flask import render_template
from flask import redirect
from flask import flash
from flask import session
from flask import url_for
from app_folder import app
from .forms import LoginForm
from .forms import RegisterForm
from app_folder.models import User, Event
from app_folder.__init__ import db
import datetime

# different URL the app will implement
@app.route("/")
# called view function
def index():
    """
    Returns the rendered 'index.html' template.

    Parameters:
        none

    Returns:
        render_template('index.html'): the rendered version of the index HTML page, which has the website title,
        a link to the login page, and a link to the create-account page

    Changelog:
        Saima 4/19: created homepage in index.html
    """
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Create address for Login page

    Returns to:
        login.html.
        forms.py for LoginForm class.
        Sign In

    Changelog:
        4/19 Ali

        Dylan 4/19: Added session username, changed flash message

        Dylan 5/3: session['username'] receiving different data to fix a bug

    """
    current_form = LoginForm()
    if current_form.validate_on_submit():
        user = User.query.filter_by(
            username=current_form.username.data).first()
        if user == None:
            flash('Incorrect username or password')
        elif current_form.password.data == user.password_hash:
            session['username'] = user.username
            flash(f'Hello {user.username}!')
            return redirect(url_for('accountHomePage'))
            exit
        else:
            flash('Incorrect username or password')
        
    return render_template('login.html', title='Sign In', form=current_form)


@app.route("/create-account", methods=['GET', 'POST'])
def createaccount():
    '''
    Create account page

    Changelog:
        Isaac 04/19: establishment of page excluding database implementation

        Dylan 5/3: Adds user to database

    '''
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                 password_hash=form.password.data)
        if User.query.filter_by(email=user.email).first() is not None:
            flash('Email already exists')
            return redirect(url_for('createaccount'))
        elif User.query.filter_by(username=user.username).first() is not None:
            flash('User name already exists')
            return redirect(url_for('createaccount'))
        else:
            session['username'] = user.username
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('accountHomePage'))
    return render_template('create-account.html', form=form)

@app.route('/logout')
def logout():
    '''
    Pops the session username

    Changelog:
        Dylan 4/19: Created initial implementation

    '''
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))


@app.route('/<username>')
def guestPage(username):
    '''
    Directs to a calendar that has information on the user's availability

    Changelog:
        Ali, Dylan 5/3: Initial implementation
    '''
    return render_template('calendar.html', days = 31, user = username)

  
@app.route('/<username>/availableTimes')
def availableTimes(username):
    '''
    Redirect to display available times

    Changelog:
        Ali, Dylan 5/3: Initial implementation
    '''
    flash('Test times')
    return redirect(f'/{username}')

  
@app.route('/meetings')
def accountHomePage():
    '''
        Displays all meeting date, time, guest, and description

    Changelog:
        Dylan 5/3: Created initial implementation
    '''
    u=User.query.filter_by(username=session['username']).first()
    e=Event.query.filter_by(creator=u).all()
    if not e:
        flash('No meetings on the horizon!')
    return render_template('meetings-page.html', events=e)
