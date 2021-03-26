from app.main import db,ma
from sqlalchemy import dialects,ForeignKey
from sqlalchemy.orm import relationship
# from .customer_model import Customer
from marshmallow import Schema, fields, ValidationError, pre_load
from sqlalchemy.dialects.postgresql import JSON

class Education(db.Model):

    __tablename__ = 'education'
    customer = relationship('Customer', back_populates='education')

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id = db.Column(db.Integer,ForeignKey("customer.id"))
    fromdate= db.Column(db.Date())
    todate = db.Column(db.Date())
    school = db.Column(db.String(50))
    description = db.Column(db.String(250))
    fieldofstudy = db.Column(db.String(250))


class Experience(db.Model):
    __tablename__ = 'experience'
    customer = relationship('Customer', back_populates='experience')

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id = db.Column(db.Integer,ForeignKey('customer.id'))
    current = db.Column(db.Boolean)
    company = db.Column(db.String(100))
    fromdate = db.Column(db.DateTime)
    todate = db.Column(db.DateTime)
    skills = db.Column(JSON)
    location = db.Column(db.String())
    title = db.Column(db.String())

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String())
    email= db.Column(db.String())
    password = db.Column(db.String())
    hash = db.Column(db.String())

    education = relationship('Education', back_populates="customer")
    experience = relationship('Experience', back_populates="customer")
    posts = relationship('Posts',back_populates="customer")
    likes = relationship('Likes', back_populates="customer")
    comments = relationship('Comments',back_populates="customer")


class Posts(db.Model):
    __tablename__ = "posts"
    customer = relationship('Customer',back_populates='posts')

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id = db.Column(db.Integer,ForeignKey('customer.id'))
    post = db.Column(db.String())

    comments = relationship('Comments', back_populates="posts")
    likes = relationship('Likes', back_populates="posts")


class Likes(db.Model):
    __tablename__ = "likes"
    customer = relationship('Customer',back_populates="likes")
    posts = relationship('Posts', back_populates="likes")

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    posts_id = db.Column(db.Integer,ForeignKey('posts.id'))
    customer_id = db.Column(db.Integer,ForeignKey('customer.id'))


class Comments(db.Model):
    __tablename__ = 'comments'
    customer = relationship('Customer',back_populates='comments')
    posts = relationship('Posts',back_populates="comments")

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    posts_id = db.Column(db.Integer,ForeignKey('posts.id'))
    customer_id = db.Column(db.Integer,ForeignKey('customer.id'))
    comment = db.Column(db.String())






