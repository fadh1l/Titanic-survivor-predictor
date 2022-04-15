import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [int_features]
    df = pd.DataFrame(final_features, columns = ['Pclass','Sex','Age','Embarked','Title'])
    prediction = model.predict(df)
    if prediction == 1:
        return render_template('index.html', prediction_text='Hurray, you\'ll live!')
    else:
        return render_template('index.html', prediction_text='Sadly, you don\'t survive..')
    

if __name__ == "__main__":
    app.run(debug=True)