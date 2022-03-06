import re
import numpy as np

class Preprocessor:
    def __init__(self, text_cleaning_re) -> None:
        self.text_cleaning_re = text_cleaning_re

    def clean_and_tokenize(self, text):

        text = re.sub(self.text_cleaning_re, '', text)
        #lowercase and whitespace tokenizer
        text = text.lower().split()
        return text

    def get_doc_vec(self, text):

        output=np.zeros(self.embedding_dim)
        numw=0
        for token in text:
            try:
                output += self.ftmodel.wv[token]
                numw+=1
            except:
                pass
        if output[0]==0:
            return output
        else:
            return output/numw


class Predictor:
    def __init__(self, mlmodel) -> None:
        self.mlmodel = mlmodel

    def predict_sentiment(self, vector):
        ml
