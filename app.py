from flask import Flask, request, render_template
from service_tools.service import Preprocessor

def init():
    global preprocessor
    text_cleaning_re = "[^A-Za-z0-9 ]+"
        # pip3 install gensim==3.8.3
    preprocessor = Preprocessor(text_cleaning_re)
    print("Initializing preprocessor...done")

init()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():

    mlmodel = request.form['mlmodel']

    if mlmodel == 'lgr':
        text = request.form['text']
        text = preprocessor.clean_and_tokenize(text)

    elif mlmodel == 'svm':
        text = request.form['text']+'hihihi'

    return render_template('index.html', prediction_text=text)

@app.route('/clear',methods=['POST'])
def clear():
    return render_template('index.html')


if __name__ == '__main__':
    #init()
    # run server
    app.run(port = 5000, debug=True)