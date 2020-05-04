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
    
    """
    current_form = LoginForm()
    if current_form.validate_on_submit():
        session['username'] = current_form.username
        flash(f'Hello {current_form.username.data}!')
        return redirect('/')
    return render_template('login.html', title='Sign In', form=current_form)



@app.route("/create-account", methods=['GET', 'POST'])
def createaccount():
    '''
    Create account page

    Changelog:
        Isaac 04/19: establishment of page excluding database implementation

    '''
    form = RegisterForm()
    if form.validate_on_submit():
        
        user = [form.email, form.username, form.password]
        db.session.add(user)
        db.commit()

        flash('You have created an account!')            
        redirect('/login')
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
    form = SettingsForm()
    if request.method == 'POST':
        return redirect('/deleteaccount')
    return render_template('settings.html', form=form)


@app.route('/deleteaccount', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    return render_template('delete-account.html', form=form)