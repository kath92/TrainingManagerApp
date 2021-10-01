from flask import Flask
from flask_restful import Api

from controllers.hello_controller import HelloController

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloController.RetrieveUpdateDelete, "/hello/<int:id>")
api.add_resource(HelloController.ListCreate, "/hello")

if __name__ == '__main__':
    app.run(debug=True)
