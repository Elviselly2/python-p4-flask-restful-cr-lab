from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Numeric)
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "image": self.image,
        "price": float(self.price) if self.price is not None else None
    }

