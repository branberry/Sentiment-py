from textblob import TextBlob

# A class to compute sentiments of given text
class Sentiment: 
    def __init__(self):
        self.sentences = {}
    
    def getSentences(self):
        return self.sentences
    
    # pass a single string as an argument
    def getSentiment(self, sent):
        pass
    # returning the sentiment value from the given list of sentences
    def getSentiments(self, key, sents):
        res = {}
        sentence = TextBlob(sents)
        res[key] = sentence.sentiment.polarity
        return res