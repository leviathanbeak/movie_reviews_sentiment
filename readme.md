## Trained Sentiment Analysis model in Python with NLTK lib
### About
Simple Flask server that predicts whether Movie Review is Positive or Negative

Returns "pos" for positive and "neg" for negative review

### How to use it
```js
// unzip sa_classifier.zip to sa_classifier.pickle
// then build and run the image with docker
$ docker build -t movie-review-sentiment:latest .
$ docker run -d -p 5000:5000 movie-review-sentiment

// then make a request either with POST or GET (info in app.py)
http://localhost:5000/predict?input="this movie was really good, actors were so-so, but movie overall was fine"

// response -> "pos"
```