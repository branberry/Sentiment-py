from flask import Flask
from flask_restful import Resource, Api, reqparse
from textblob import TextBlob

app = Flask(__name__)
api = Api(app)


class TestModel(Resource):
    def post(self):
        return {}

class HelloWorld(Resource):
    def get(self):
        res = {}
        wiki = TextBlob("Python is a high-level, general-purpose programming language.")
        res['textblob'] = wiki.sentiment
        return res

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)