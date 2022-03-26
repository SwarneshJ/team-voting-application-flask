from flask_sqlalchemy import SQLAlchemy

# create a new SQLAlchemy object
db = SQLAlchemy()

class EmailList(db.Model):
    email = db.Column(db.String(100), primary_key=True)

    def __init__(self, email):
        self.email = email

    def to_json(self):
        return {
            'email': self.email
        }

class TeamMember(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    count = db.Column(db.Integer)

    def __init__(self, name, id,title, count):
        self.name = name
        self.id = id
        self.title = title
        self.count = count

    def to_json(self):
        return {
            'name': self.name,
            'id': self.id,
            'title': self.title,
            'count': self.count
        }