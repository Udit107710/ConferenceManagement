import sqlalchemy as db
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from flask_appbuilder import Model
import uuid
import re
from datetime import datetime

speakers = db.Table('speakers', Model.metadata,
    db.Column('speaker_id', db.String(120), db.ForeignKey('speaker.username'), primary_key=True),
    db.Column('talk_id', UUID(as_uuid=True), db.ForeignKey('talk.id'), primary_key=True),
)

participants = db.Table('participants', Model.metadata,
    db.Column('participant_id', db.String(120), db.ForeignKey('participant.username'), primary_key=True),
    db.Column('talk_id', UUID(as_uuid=True), db.ForeignKey('talk.id'), primary_key=True),
)

class Speaker(Model):
    username = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=True)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", username):
            raise AssertionError('Provided username is not an email address')
        return username

    def __repr__(self):
        return '<Speaker %r>' % self.username


class Participant(Model):
    username = db.Column(db.String(120), unique=True, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=True)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", username):
            raise AssertionError('Provided username is not an email address')
        return username

    def __repr__(self):
        return '<Participant %r>' % self.username


class Talk(Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=True) # In minutes
    start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    conference_id = db.Column(UUID(as_uuid=True), db.ForeignKey('conference.id'), nullable=False)

    speakers = db.orm.relationship('Speaker', secondary=speakers, lazy='subquery', backref='talks')
    participants = db.orm.relationship('Participant', secondary=participants, lazy='subquery', backref='talks')


class Conference(Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    talks = db.orm.relationship('Talk', backref='conference', lazy=True)
