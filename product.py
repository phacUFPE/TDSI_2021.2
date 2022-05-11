from app import db
from constants import DatabaseConstants


class Product(db.Model):
    __tablename__ = DatabaseConstants.PRODUCT_TABLE_NAME
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name
