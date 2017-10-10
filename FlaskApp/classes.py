from flask_sqlalchemy import SQLAlchemy

class Energy(db.Model):
    __tablename__='energy'
    tweet_id = db.Column('tweet_id', db.Unicode, primary_key=True)
    date_time = db.Column('date_time', db.Datetime)
    lang = db.Column('lang', db.Unicode)
    text = db.Column('text', db.Unicode)
    city = db.Column('city', db.Unicode)
    country = db.Column('country', db.Unicode)
    user = db.Column('user', db.Unicode)

class Construction(db.Model):
    __tablename__='energy'
    tweet_id = db.Column('tweet_id', db.Unicode, primary_key=True)
    date_time = db.Column('date_time', db.Datetime)
    lang = db.Column('lang', db.Unicode)
    text = db.Column('text', db.Unicode)
    city = db.Column('city', db.Unicode)
    country = db.Column('country', db.Unicode)
    user = db.Column('user', db.Unicode)

class Oil(db.Model):
    __tablename__='energy'
    tweet_id = db.Column('tweet_id', db.Unicode, primary_key=True)
    date_time = db.Column('date_time', db.Datetime)
    lang = db.Column('lang', db.Unicode)
    text = db.Column('text', db.Unicode)
    city = db.Column('city', db.Unicode)
    country = db.Column('country', db.Unicode)
    user = db.Column('user', db.Unicode)
