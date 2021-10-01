from flask_restful.reqparse import RequestParser


class ModelParser:
    def __init__(self, model_type):
        self.model_type = model_type
        self.request_parser = RequestParser()

    def parse_model(self):
        args = self.request_parser.parse_args(strict=True)
        model = self.model_type()
        model.__dict__.update(args)
        return model
