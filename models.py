from mongoengine import *
from flask_mongoengine import MongoEngine

db = MongoEngine()


class OneImage(db.EmbeddedDocument):
    element = db.ImageField(thumbnail_size=(100, 100, True))

    def get_el(self):
        return self.element.name


class UserV(db.Document):
    second_name = db.StringField(required=True, max_length=50)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    image = ImageField(thumbnail_size=(200, 200, True))
    image2 = db.ListField(db.EmbeddedDocumentField(OneImage))
    image3 = db.StringField(required=False, max_length=500)
