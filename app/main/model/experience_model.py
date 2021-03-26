from app.main import db
from sqlalchemy import ForeignKey, dialects
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
# from .customer_model import Customer

class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer = relationship ('Customer', back_populates="experience")
    customer_id = db.Column(db.Integer,ForeignKey('customer.id'))
    current = db.Column(db.Boolean)
    company = db.Column(db.String(100))
    fromdate = db.Column(db.DateTime)
    todate = db.Column(db.DateTime)
    skills = db.Column(JSON)
    location = db.Column(db.String())
    title = db.Column(db.String())