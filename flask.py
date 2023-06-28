from flask import Flask, request, jsonify, render_template, url_for
import pickle
import numpy as np
import json
app = Flask(__name__)
#Loading the pickel file
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def man():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def home():
    d1=request.form['a']
    d2=request.form['b']
    d3=request.form['c']
    d4=request.form['d']
    d5=request.form['e']
    d6=request.form['f']
    d7=request.form['g']
    d8=request.form['h']
    d9=request.form['i']
    d10=request.form['j']
    d11=request.form['k']
    d12=request.form['l']
    d13=request.form['m']
    

    arr=np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]])
    pred=model.predict(arr)
    return render_template("after.html", data=pred)

if __name__ == "__main__":
    app.run(debug=True)