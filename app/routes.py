from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # processing work
    # GET --> False --> render template
    # POST --> gather all data and run all validators --> if all good, return True
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)