from flask import Flask
from flask_restful import Resource, Api, reqparse
from textblob import TextBlob

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text')
class TestModel(Resource):
    def post(self):
        res = {}
        args = parser.parse_args()
        res['text'] = args['text']
        return res, 201

class HelloWorld(Resource):
    def get(self):
        return {
            'hello' : 'world'
        }

api.add_resource(HelloWorld, '/')
api.add_resource(TestModel,'/test')
if __name__ == '__main__':
    app.run(debug=True)