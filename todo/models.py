from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from todo.database import Base
from todo import app

db = SQLAlchemy(app)


class Entry(db.Model):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    order = Column(Integer)
    completed = Column(Boolean)

    def __init__(self, title=None, order=None):
        self.title = title
        self.order = order
        self.completed = False

    def __repr__(self):
        return "<Entry: {}>".format(self.title)


db.create_all()
db.session.commit()
