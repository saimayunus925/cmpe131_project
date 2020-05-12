from flask import render_template
from flask import redirect
from flask import flash
from flask import request
from flask import session
from flask import url_for
from app_folder import app
from .forms import LoginForm
from .forms import RegisterForm
from .forms import SettingsForm
from .forms import DeleteForm
from .forms import ScheduleMeetingForm
from .forms import MeetingDescriptionForm
from app_folder.models import User, Event
from app_folder import db
import datetime
from app_folder import funcs


# different URL the app will implement
@app.route("/")
# called splash function
def splash():
    """
    Returns the rendered 'splash_page.html' template.
    Parameters:
        none
    Returns:
        the splash page ot the website, contains details about what the site does as well as pictures outlining each feature
    Changelog:
        Isaac 5/10: created splash page in splash_page.html
    """

    return render_template('splash_page.html')


@app.route("/home")
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
        Dylan 5/10: Password encryption
    """
    current_form = LoginForm()
    if current_form.validate_on_submit():
        user = User.query.filter_by(
            username=current_form.username.data).first()
        if user == None:
            flash('Incorrect username or password')
        elif funcs.checkPswd(user, current_form.password.data):
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
        Dylan 5/10: Password encryption
    '''
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        if User.query.filter_by(email=user.email).first() is not None:
            flash('Email already exists')
            return redirect(url_for('createaccount'))
        elif User.query.filter_by(username=user.username).first() is not None:
            flash('User name already exists')
            return redirect(url_for('createaccount'))
        else:
            funcs.createNewPswd(user, form.password.data)
            session['username'] = user.username
            db.session.add(user)
            db.session.commit()
            flash("Account created.")
            flash(f'Hello {user.username}!')
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


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    '''
    Deletes user from database
    
    Changelog:
        Dylan 5/11: Now actually changes user settings
    '''
    form = SettingsForm()
    user = User.query.filter_by(username=session['username']).first()
    if request.method == 'POST':
        if form.delete.data:
            return redirect('/deleteaccount')
        elif form.submit.data:
            user.start_time = datetime.datetime.strptime(form.start_time_of_day.data, '%H').time()
            user.end_time = datetime.datetime.strptime(form.end_time_of_day.data, '%H').time()
            user.meeting_length = form.timeops.data
            db.session.add(user)
            db.session.commit()
            flash('Settings changed.')
            return redirect('/meetings')
    return render_template('settings.html', form=form)


@app.route('/deleteaccount', methods=['GET', 'POST'])
def delete():
    '''
    Deletes user from database
    
    Changelog:
        Dylan 5/3: Database functionality added
        Dylan 5/10: Password encryption
    '''
    form = DeleteForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=session['username']).first()
        if form.username.data == user.username and funcs.checkPswd(user, form.password.data):
            session.pop('username', None)
            db.session.delete(user)
            db.session.commit()
            flash("Account successfully deleted.")
            return redirect(url_for('index'))
    return render_template('delete-account.html', form=form)


@app.route('/<username>', methods=['GET', 'POST'])
def guestPage(username):
    '''
    Directs to a calendar that has information on the user's availability
    Changelog:
        Ali, Dylan 5/3: Initial implementation
        Dylan 5/11: Properly gains date information
    '''
    user = User.query.filter_by(username=username).first_or_404()
    form = ScheduleMeetingForm()
    if request.method == 'POST':
        return redirect(f'/{username}/{form.date.data.strftime("%m%d%y")}/availableTimes')
    return render_template('scheduleMeeting.html', form=form)
    #return render_template('calendar.html', days = 31, user = username)

  
@app.route('/<username>/<date>/availableTimes', methods=['GET', 'POST'])
def availableTimes(username, date):
    '''
    Redirect to display available times
    Changelog:
        Ali, Dylan 5/3: Initial implementation
        Dylan 5/11: Properly displays times
    '''
    #flash('Test times')
    form = MeetingDescriptionForm()
    user = User.query.filter_by(username=username).first()
    strp_date = datetime.datetime.strptime(date, '%m%d%y')
    form.time.choices = funcs.generateAvailability(user, strp_date)
    if request.method == 'POST':
        e = Event(user_id=user.id,
            datetime=datetime.datetime.combine(strp_date, datetime.datetime.strptime(form.time.data, '%H:%M:%S').time()),
            guest_name=form.name.data)
        if form.description.data is not None:
            e.description = form.description.data

        db.session.add(e)
        db.session.commit()
        flash('Your meeting was successfully scheduled!')
        return redirect(url_for('index'))
    
    return render_template('meetingDescription.html', form=form, head=f'{username}: {strp_date.strftime("%m/%d/%y")}')

  
@app.route('/meetings')
def accountHomePage():
    '''
        Displays all meeting date, time, guest, and description
    Changelog:
        Dylan 5/3: Created initial implementation
        Dylan 5/11: Properly queries databases and shows only future events.
    '''
    u=User.query.filter_by(username=session['username']).first()
    events=Event.query.filter_by(creator=u).all()
    for e in events:
        if e.datetime < datetime.datetime.now():
            db.session.remove(e)
            events.remove(e)
            db.session.commit()
    if not events:
        flash('No meetings on the horizon!')
    return render_template('meetings-page.html', events=events)