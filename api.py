from flask import Flask, Blueprint
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource
from models import UserV
import json


db = MongoEngine()


app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_db',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)


class ShowAllUsers(Resource):
    def get(self):
        users = UserV.objects()
        return json.loads(users.to_json())


class ShowUser(Resource):
    '''Выборка 1 пользователя по ID'''
    def get(self, pk):
        user = UserV.objects(id=pk)
        return json.loads(user.to_json())


api.add_resource(ShowAllUsers, '/show/')
api.add_resource(ShowUser, '/show_user/<pk>')
