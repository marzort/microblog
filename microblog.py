import sqlalchemy as sa
import sqlalchemy.orm as so
# imports the app variable that is a member of the app package
from app import app, db
from app.models import User, Post

# decorator that registers the function as a shell context function
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}