from app import db

'''
for creating the database and create some db records
you need to open the terminal (cmd) and do the following
python3 
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
/home/rhyme/.local/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:834: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()
>>> from models import Task
>>> from datetime import datetime
>>> t = Task(title="something", date=datetime.utcnow())
>>> t
something created on 2021-08-22 20:36:27.541135
>>> exit()


'''

class Task(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date  = db.Column(db.Date, nullable=False)

    # this is prerequesite for the Model
    def __repr__(self):
        return f'{self.title} created on {self.date}'

