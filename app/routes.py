from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)