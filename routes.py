from app import myFlaskObj
from flask import render_template
from app.forms import LoginForm
from app.forms import createAccountForm
from app.forms import LogOutForm
from flask import flash

@myFlaskObj.route('/')
def hello():
    username = ' =)'
    someList = ['11','22','33','66']
    return render_template('index.html', indexUsr = username, indexLst = someList)

@myFlaskObj.route('/createAccount', methods=['GET','Post'])
def createAccount():
    form = createAccountForm()
    if form.validate_on_submit():
        flash('You Created An Account!', 'Hoo')
        flash('Woo!')
    return render_template('createAccount.html', form=form)

# Display After Clicked Sign-On button
@myFlaskObj.route('/login', methods=['GET','Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You Logged-In!', 'Hoo')
        
    return render_template('login.html', form=form)

@myFlaskObj.route('/logout', methods=['GET','Post'])
def logout():
    form = LogOutForm()
    if form.validate_on_submit():
        flash('You Logged-Out!', 'Hoo')
    return render_template('logout.html', form=form)

