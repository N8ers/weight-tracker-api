from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello_World(Resource):
    def get(self, message):
        return {"message": message}


api.add_resource(Hello_World, "/hello/<string:message>")

app.run(port=5000)
