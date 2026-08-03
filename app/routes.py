from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maria'}
    posts = [
        {
            'author': {'username': 'Jongho'},
            'body': 'Beautiful day in Seoul!'
        },
        {
            'author': {'username': 'Yunho'},
            'body': 'The Spiderman movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
# render_template() takes a template filename and a variable list of template arguments
# and returns the same template, but with all the placeholders in it replaced with actual values

@app.route('/login', methods=['GET', 'POST']) # override default methods accepted
def login():
    form = LoginForm()
    # processing work
    # GET --> False --> render template
    # POST --> gather all data and run all validators --> if all good, return True
    if form.validate_on_submit():
        # flash() will show a message to the user to confirm input
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # redirect() tells client's web browser to auto navigate to different page
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)