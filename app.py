from flask import Flask, request, render_template
from service_tools.service import Predictor, Preprocessor

app = Flask(__name__)

#initialize Preprocessor class
preprocessor = Preprocessor()
#initialize Predictor class
predictor = Predictor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    mlmodel = request.form['mlmodel']
    text = request.form['text']
    doc_vec = preprocessor.get_doc_vec(text)
    sentiment = predictor.predict_sentiment(mlmodel, doc_vec)

    return render_template('index.html',entered_text = "Entered Review:",
    original_text = text, prediction_text=sentiment)


if __name__ == '__main__':
    # run server
    app.run(host = "140.112.147.112", port = 3000, debug=True)