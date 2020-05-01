from app import db

class User(db.Model):
    applicatio_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    Messages = db.relationship('Message', backref='author', lazy='dynamic')
    def as_dict(self):
        return {
        'applicatio_id': self.applicatio_id,
        'username': self.username,
        }

class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.applicatio_id'))
    session_id = db.Column(db.String(50))
    participants = db.Column(db.PickleType)
    def as_dict(self):
        return {
        'message_id': self.message_id,
        'content': self.content,
        'user_id': self.user_id,
        'session_id': self.session_id,
        }   

               