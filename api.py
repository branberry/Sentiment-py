from flask import Flask
from flask_restful import Resource, Api, reqparse

from nlp.Sentiment import Sentiment

import json

app = Flask(__name__)
api = Api(app)

# creating the parser to handle request data 
parser = reqparse.RequestParser()

# test argument
parser.add_argument('text')

# this will be used to test NLP model code
parser.add_argument('sentences')

#  Using this model to handle NLP requests
class SentimentModel(Resource):
    def post(self):
        # the sentiment object that contains our methods
        sentimentAnalyzer = Sentiment()
        # retreiving the data from the POST request
        args = parser.parse_args()
        
        # convert sentences JSON object to dict
        sentences = json.load(args['sentences'])
        # computing the sentiments!
        res = sentimentAnalyzer.getSentiments(sentences)      

        return res
class TestModel(Resource):
    def post(self):
        res = {}
        args = parser.parse_args()
        res['text'] = args['text']
        return res

class HelloWorld(Resource):
    def get(self):
        return {
            'hello' : 'world'
        }

api.add_resource(HelloWorld, '/')
api.add_resource(TestModel,'/test')
api.add_resource(SentimentModel,'/sentiments')

if __name__ == '__main__':
    app.run(debug=True)