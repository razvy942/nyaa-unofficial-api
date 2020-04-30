from backend.extensions import db

watching = db.Table('watch_queue',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('series_id', db.Integer, db.ForeignKey('series.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    watch_queue = db.relationship('Series', secondary=watching, backref=db.backref('viewers', lazy= 'dynamic'))

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kitsu_id = db.Column(db.Integer, nullable=False)
    canonical_title = db.Column(db.String(120), unique=True, nullable=False)
    en_title = db.Column(db.String(120), unique=True, nullable=False)
    en_jp_title = db.Column(db.String(120), unique=True, nullable=False)
    attributes = db.relationship('Attributes', backref='series', lazy=True)


class Attributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    synopsis = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    start_date = db.Column(db.String(15), nullable=False)
    end_time = db.Column(db.String(15))
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)