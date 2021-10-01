from flask_restful import Resource, marshal_with

from models.user import User
from utils.authentication import auth
from utils.model_schema import USER_FIELDS, USER_PARSER

users = []


class UserController:
    class RetrieveUpdateDelete(Resource):
        # @auth.login_required
        # @marshal_with(USER_FIELDS)
        def get(self, id):
            pass

        def put(self, id):
            pass

        def delete(self, id):
            pass

    class ListCreate(Resource):
        pass

        def post(self):
            pass