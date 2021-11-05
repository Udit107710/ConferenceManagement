from flask_appbuilder import ModelRestApi
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask import request
from .models import Talk as TalkModel , Conference as ConferenceModel , Speaker as SpeakerModel , Participant as ParticipantModel
from app import appbuilder
from app import db
# from .schemas import SpeakerSchema, ParticpantSchema, ConferenceSchema, TalkSchema

class Speaker(ModelRestApi):
    resource_name = 'speaker'
    # add_model_schema = SpeakerSchema()
    # edit_model_schema = SpeakerSchema()
    datamodel = SQLAInterface(SpeakerModel)
    add_columns = ('username', 'name')
    exclude_route_methods = ("delete")


class Participant(ModelRestApi):
    resource_name = 'participant'
    # add_model_schema = ParticpantSchema()
    # edit_model_schema = ParticpantSchema()
    datamodel = SQLAInterface(ParticipantModel)
    add_columns = ('username', 'name')
    exclude_route_methods = ("delete")


class Talk(ModelRestApi):
    resource_name = 'talk'
    # add_model_schema = TalkSchema()
    # edit_model_schema = TalkSchema()
    datamodel = SQLAInterface(TalkModel)
    exclude_route_methods = ("delete")
    base_order = ('title', 'desc')


class Conference(ModelRestApi):
    resource_name = 'conference'
    # add_model_schema = ConferenceSchema()
    # edit_model_schema = ConferenceSchema()
    datamodel = SQLAInterface(ConferenceModel)
    exclude_route_methods = ("delete")
    base_order = ('title', 'desc')


class TalkParticipantAPI(BaseApi):

    resource_name = 'talk'

    @expose('participants/add', methods=['POST'])
    def add_participants(self):
        talk_id = request.args.get('talk')
        data = request.json
        participants = db.session.query(ParticipantModel).filter(ParticipantModel.username.in_(data['participants'])).all()
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id).one()
        talk.participants.extend(participants)
        db.session.commit()
        return self.response(200, message="Successfully added participants")

    @expose('participants/remove', methods=['POST'])
    def remove_participants(self):
        talk_id = request.args.get('talk')
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id)
        data = request.json
        participants = db.session.query(ParticipantModel).filter(ParticipantModel.username.in_(data['participants'])).all()
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id).one()
        for participant in participants:
            talk.participants.remove(participant)
        db.session.commit()
        return self.response(200, message="Successfully removed participants")

class TalkSpeakerAPI(BaseApi):

    resource_name = 'talk'

    @expose('speakers/add', methods=['POST'])
    def add_speakers(self):
        talk_id = request.args.get('talk')
        data = request.json
        speakers = db.session.query(SpeakerModel).filter(SpeakerModel.username.in_(data['speakers'])).all()
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id).one()
        talk.speakers.extend(speakers)
        db.session.commit()
        return self.response(200, message="Successfully added speakers")

    @expose('speakers/remove', methods=['POST'])
    def remove_speakers(self):
        talk_id = request.args.get('talk')
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id)
        data = request.json
        speakers = db.session.query(SpeakerModel).filter(SpeakerModel.username.in_(data['speakers'])).all()
        talk = db.session.query(TalkModel).filter(TalkModel.id == talk_id).one()
        for speaker in speakers:
            talk.speakers.remove(speaker)
        db.session.commit()
        return self.response(200, message="Successfully removed speakers")

# db.create_all() # Only when running the first time
appbuilder.add_api(Speaker)
appbuilder.add_api(Participant)
appbuilder.add_api(Talk)
appbuilder.add_api(Conference)
appbuilder.add_api(TalkParticipantAPI)
appbuilder.add_api(TalkSpeakerAPI)