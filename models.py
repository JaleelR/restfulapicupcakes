"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    
    id = db.Column(db.Integer,
                   primary_key=True, 
                   autoincrement = True)
    flavor = db.Column(db.Text, 
                   nullable=False)
    size = db.Column(db.Text, 
                    nullable=False)
    rating = db.Column(db.Float, 
                    nullable=False)
    image = db.Column(db.Text,
                    nullable=True)


def serialized_cupcakes(cupcake):
    """ serialize a cupcake sqlalchemy obj to dictionary """

    return {
            "id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image

        }