from app.main import db, ma
from sqlalchemy.dialects.postgresql import JSON
from marshmallow import Schema, fields, ValidationError, pre_load
from sqlalchemy.orm import relationship
from .education_model import Education,Customer,Experience,Posts,Comments,Likes


class EducationSchema(ma.ModelSchema):
    class Meta:
        model = Education
        sqla_session = db.session


class ExperienceSchema(ma.ModelSchema):
    class Meta:
        model = Experience
        sqla_session = db.session

class CommentsSchema(ma.ModelSchema):
    class Meta:
        model = Comments

class LikesSchema(ma.ModelSchema):
    class Meta:
        model = Likes

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Posts
        sqla_session = db.session
    comments = fields.Nested(CommentsSchema,many=True)
    likes = fields.Nested(LikesSchema,many=True)

class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
    experience = fields.Nested(ExperienceSchema, many=True)
    education = fields.Nested(EducationSchema, many=True)
    posts = fields.Nested(PostSchema,many=True)
