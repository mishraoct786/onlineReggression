import pickle
import numpy as np
from flask import Flask,jsonify,render_template,request
app =Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_feature=[int (x) for x in request.form.values()]
    final_features=[np.array(int_feature)]
    prediction=model.predict(final_features)
    output=prediction
    return render_template('home.html',prediction_text="employe salay should be {}".format(output))

@app.route('/courses')
def courses():
    return "<h1>Flask basic tutorial</h1>"

from flask import render_template

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()

