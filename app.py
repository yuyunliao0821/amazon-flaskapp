from flask import Flask, request, render_template
from service_tools.service import Predictor, Preprocessor
from gensim.models import FastText
import joblib

def init():
    #initialize Preprocessor class
    print("Initializing preprocessor...")
    global preprocessor
    text_cleaning_re = "[^A-Za-z0-9 ]+"
        # pip3 install gensim==3.8.3
    ft_model = FastText.load('models/ft_model.model')
    preprocessor = Preprocessor(text_cleaning_re, ft_model)
    print("DONE")

    #initialize Predictor class
    print("Initializing predictor...")
    global predictor
    lgr_model = joblib.load("models/lgr.pkl")
    svm_model = joblib.load("models/svm.pkl")
    predictor = Predictor(lgr_model, svm_model)
    print("DONE")

init()

app = Flask(__name__)

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
    #init()
    # run server
    app.run(host = "140.112.147.112", port = 3000, debug=True)