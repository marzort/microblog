from typing import Optional
# includes general purpose db functions and classes like types and query builders
import sqlalchemy as sa
# provides support for using models
import sqlalchemy.orm as so
from app import db

# represents users stored in db; inherits from base class db.Model
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # tells Python how to print objects of this class; good for debugging
    def __repr__(self):
        return '<User {}>'.format(self.username)