import re
import numpy as np
import sklearn


class Preprocessor:
    def __init__(self, text_cleaning_re, ft_model):
        self.text_cleaning_re = text_cleaning_re
        self.ft_model = ft_model
        

    #clean and tokenize text, helper function for get_doc_vec
    def clean_and_tokenize(self, text):

        text = re.sub(self.text_cleaning_re, '', text)
        #lowercase and simple whitespace tokenizer
        text = text.lower().split()
        return text

    def get_doc_vec(self, text):
        """
        text : raw text entered in input textbox
        """
        text = self.clean_and_tokenize(text)
        output=np.zeros(64)
        numw=0
        for token in text:
            try:
                output += self.ft_model.wv[token]
                numw+=1
            except:
                pass
        if output[0]==0:
            return output
        else:
            return output/numw

class Predictor:
    def __init__(self, lgr_model, svm_model):
        self.lgr_model = lgr_model
        self.svm_model = svm_model

    def predict_sentiment(self, mlmodel, vector):
        """
        mlmodel : string. used to specify prediction model type; available options:'lgr','svm'
        vector : document vector. result from get_doc_vec()
        """
        if mlmodel == 'lgr':
            prediction = self.lgr_model.predict([vector])
        elif mlmodel == 'svm':
            prediction = self.svm_model.predict([vector])
        
        if prediction == 1:
            return "This review seems to be positive😇 !!"
        else:
            return "This review seems to be negative😨 !!"
        