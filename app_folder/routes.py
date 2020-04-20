from flask import render_template
from flask import redirect
from flask import flash
from flask import session
from flask import url_for
from app_folder import app
from .forms import LoginForm

# different URL the app will implement
@app.route("/")
# called view function
def index():
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

@app.route('/logout')
def logout():
    '''
    Session logout
    Dylan 4/19: Created initial implementation

    '''
    session.pop('username', None)
    return redirect(url_for('index'))