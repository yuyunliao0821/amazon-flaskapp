from flask import Flask, request, render_template, jsonify
from service_tools.service import Predictor, Preprocessor

app = Flask(__name__)

#initialize Preprocessor class
preprocessor = Preprocessor()
#initialize Predictor class
predictor = Predictor()

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     print(request.args)
#     if 'text' in request.args:
#         text = request.args['text']
#     if 'mlmodel' in request.args:
#         mlmodel = request.args['mlmodel']
#         print(mlmodel)
    
#     return text+mlmodel
@app.route('/predict', methods=['POST'])
def predict():
    result = request.get_json()[0]
    result = result['text']+result['mlmodel']+'ajax is working!'
    print(result)

    return jsonify(result)

if __name__ == '__main__':
    # run server
    app.run(host = "140.112.147.112", port = 3000, debug=True)