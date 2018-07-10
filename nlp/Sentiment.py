from textblob import TextBlob

# A class to compute sentiments of given text
class Sentiment: 
    def __init__(self):
        self.sentences = {}
    
    def getSentences(self):
        return self.sentences
    
    # returning the sentiment value from the given list of sentences
    def getSentiment(self, sents):
        res = {}
        for k,v in sents.items():
            sentence = TextBlob(v)
            res[v] = sentence.sentiment.polarity
        return res