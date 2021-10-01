from utils.model_parser import ModelParser


class ParserFactory:
    @staticmethod
    def create(model_type, args):
        parser = ModelParser(model_type)
        for arg in args.items():
            parser.request_parser.add_argument(arg[0], type=arg[1])
        return parser
