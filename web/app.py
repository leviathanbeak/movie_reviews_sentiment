import pickle
import sys
from flask import Flask, request, render_template
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
import re

from nltk.util import everygrams

lemmatizer = WordNetLemmatizer()

import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from string import punctuation

stopwords_eng = stopwords.words('english')

model_file = open('web/sa_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()
 
app = Flask(__name__) 

def bag_of_words(words):
    bag = {}
    for w in words:
        bag[w] = bag.get(w,0)+1
    return bag

def extract_features(document):
    words = word_tokenize(document)
    lemmas = [str(lemmatizer.lemmatize(w)) for w in words if w not in stopwords_eng and w not in punctuation]
    document = " ".join(lemmas)
    document = document.lower()
    document = re.sub(r'[^a-zA-Z0-9\s]', ' ', document)
    words = [w for w in document.split(" ") if w!="" and w not in stopwords_eng and w not in punctuation]
    return [str('_'.join(ngram)) for ngram in list(everygrams(words, max_len=3))]

def get_sentiment(review):
    words = extract_features(review)
    words = bag_of_words(words)
    return model.classify(words)
 
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        input = request.args.get('input')
    else:
        input = request.get_json(force=True)['input']
    if not input:
        return 'No input value found'
    return get_sentiment(input)
 
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0')