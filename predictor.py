import pickle
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import numpy as np
import pandas as pd 

tokenizer = Tokenizer()
with open('tok.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
labels = np.array(['balance_check', 'provide_information', 'raising_ticket',
       'request_acc_number', 'request_name', 'service_fulfillment',
       'small_talk']) 
print("Enter a sentence:\n")
test = input()
test = pd.Series(test)
model = load_model("model.h5")
maxlen= 200
sequences = tokenizer.texts_to_sequences(test)
test_sequences_matrix = sequence.pad_sequences(sequences, maxlen= maxlen)
prediction = model.predict(np.array(test_sequences_matrix))
predicted_label = labels[np.argmax(prediction[0])]
print(predicted_label)