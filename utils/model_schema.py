from flask_restful import fields

from models.hello import Hello
from models.user import User
from utils.parser_factory import ParserFactory

HELLO_FIELDS = {
    "id": fields.Integer,
    "message": fields.String
}

HELLO_PARSER = ParserFactory.create(Hello, {
    "message": str
})

USER_FIELDS = {
    "id": fields.Integer,
    "email": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "org_number": fields.Integer,
    # TO-DO: department & company - ForeignKey?
}

USER_PARSER = ParserFactory.create(User, {
    "email": str,
    "first_name": str,
    "last_name": str,
    # TO-DO: ForeignKey
    "org_number": int,
})
