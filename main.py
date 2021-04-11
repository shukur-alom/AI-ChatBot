from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle,random
import numpy as np
import pandas as pd

model = load_model("chatbot_model.h5")
t_n = pickle.load(open("Tokenizer.p", "rb" ))
l_e = pickle.load(open("LabelEncoder.p", "rb" ))
data = pd.read_json('intents.json')

def preprocess(text):
  t_n_x = t_n.texts_to_sequences([text])
  return pad_sequences(t_n_x,maxlen=8,padding='post')

def main_response(text):
    pri = model.predict(preprocess(text.lower()))
    if pri[0][np.argmax(pri)]*100 >= 70.00:
        for i in data['intents']:
            if i['tag'] == l_e.inverse_transform([np.argmax(pri)])[0]:
                return f"==> {random.choice(i['responses'])}"
                break
    else:return "Bot ==> Sorry, Don't able to response this message!"

if __name__ == "__main__":
    while 1:
        print(main_response(input("==> ")))
