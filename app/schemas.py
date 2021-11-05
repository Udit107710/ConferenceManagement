# from flask_appbuilder.api.schemas import BaseModelSchema
# from marshmallow import fields, post_dump, ValidationError
# from .models import Participant as ParticipantModel, Speaker as SpeakerModel, Conference as ConferenceModel, Talk as TalkModel
# import re


# class ParticpantSchema(BaseModelSchema):
#     model_cls = ParticipantModel
#     username = fields.Email()
#     name = fields.Str(required=False)

# class SpeakerSchema(BaseModelSchema):
#     model_cls = SpeakerModel
#     username = fields.Email()
#     name = fields.Str(required=False)

# class TalkSchema(BaseModelSchema):
#     model_cls = TalkModel
#     id = fields.Integer(dump_only=True)
#     title = fields.Str(required=True)
#     description = fields.Str(required=False)
#     duration = fields.Integer(required=False)
#     start = fields.DateTime(required=False)
#     conference = fields.Integer(required=False, load_only=True)

#     speakers = fields.Raw()
#     participants = fields.Raw()
#     @post_dump()
#     def add_count(self, data, **kwargs):
#         data['speakers'] = {'count': len(data['speakers']), 'results': data['speakers']}
#         data['participants'] = {'count': len(data['participants']), 'results': data['participants']}
#         return data

# class ConferenceSchema(BaseModelSchema):
#     model_cls = ConferenceModel
#     id = fields.Integer(dump_only=True)
#     title = fields.Str(required=True)
#     description = fields.Str(required=False)
#     start_date = fields.DateTime(required=False)
#     end_date = fields.DateTime(required=False)
#     talks = fields.Nested(TalkSchema, many=True, only=['id', 'title'], required=False)

#     @post_dump()
#     def add_count(self, data, **kwargs):
#         data['talks'] = {'count': len(data['talks']), 'results': data['talks']}
#         return data
