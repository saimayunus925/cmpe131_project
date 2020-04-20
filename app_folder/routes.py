from flask import render_template
from flask import redirect
from flask import flash
from flask import session
from flask import url_for
from app_folder import app
from .forms import LoginForm
from .forms import Registerform

# different URL the app will implement
@app.route("/")
# called view function
def index():
    """
    Returns the rendered 'index.html' template. 
    Saima 4/19: created homepage in index.html

    Parameters: 
        none

    Returns: 
        render_template('index.html'): the rendered version of the index HTML page, which has the website title,
        a link to the login page, and a link to the create-account page
    """
    return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])

def login():
    '''
    Login page of the app.
    Dylan 4/19: Added session username

    '''
    current_form = LoginForm()
    if current_form.validate_on_submit():
        session['username'] = current_form.username
        flash(f'Login requested for user {current_form.username.data}')
        return redirect('/')
    return render_template('login.html', title='Sign In', form=current_form)



@app.route("/create-account", methods=['GET', 'POST'])

def createaccount():
    '''
    Create account page
    Isaac 04/19: establishment of page excluding database implementation

    '''
    form = Registerform()
    if form.validate_on_submit():
        flash('You have created an account!')
    return render_template('create-account.html', form=form)



@app.route('/logout')
def logout():
    '''
    Session logout
    Dylan 4/19: Created initial implementation

    '''
    session.pop('username', None)
    return redirect(url_for('index'))