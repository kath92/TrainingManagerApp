from flask_restful import Resource, marshal_with

from models.hello import Hello
from utils.authentication import auth
from utils.model_schema import HELLO_FIELDS, HELLO_PARSER

helloes = [
    Hello(1, "Hello from Flask-RESTful!"),
    Hello(2, "Hello again!"),
    Hello(3, "This is another one!")
]


class HelloController:
    class RetrieveUpdateDelete(Resource):
        @auth.login_required
        @marshal_with(HELLO_FIELDS)
        def get(self, id):
            return helloes[id - 1]

        @auth.login_required
        @marshal_with(HELLO_FIELDS)
        def put(self, id):
            hello_from_server = helloes[id - 1]
            hello_from_client = HELLO_PARSER.parse_model()
            hello_from_server.message = hello_from_client.message
            return hello_from_server, 201

        @auth.login_required
        def delete(self, id):
            del helloes[id - 1]
            return "", 204

    class ListCreate(Resource):
        @auth.login_required
        @marshal_with(HELLO_FIELDS)
        def get(self):
            return helloes

        @auth.login_required
        @marshal_with(HELLO_FIELDS)
        def post(self):
            hello = HELLO_PARSER.parse_model()
            hello.id = max(helloes, key=lambda h: h.id).id + 1
            helloes.append(hello)
            return hello, 201
