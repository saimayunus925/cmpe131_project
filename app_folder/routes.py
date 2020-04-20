from app_folder import myFlaskObj
from flask import render_template
from flask import redirect
from flask import flash
from app_folder import app
from app_folder.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Create address for Login page
    
    Returns to: 
        login.html.
        forms.py for LoginForm class.
        Sign In
    
    4/19 Ali
    
    """
    
    
    
    current_form = LoginForm()
    if current_form.validate_on_submit():
        flash(f'Login requested for user {current_form.username.data}')
        return redirect('/')
    return render_template('login.html', title='Sign In', form=current_form)
