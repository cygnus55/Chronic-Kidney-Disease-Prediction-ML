from crypt import methods
import os
import pickle

import sklearn

from flask import Flask, render_template, request, redirect, url_for
from forms import SubmissionForm


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

with open("../models/dt_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    form = SubmissionForm()
    return render_template("index.html", form=form)


@app.route("/result", methods=["POST","GET"])
def result():
    if request.method=='POST':
        input_values=request.form.to_dict()
        del input_values['csrf_token']
        input_values=list(input_values.values())
        input_values=list(map(float,input_values))
        print(input_values)
        final='No CKD' if model.predict([input_values])[0] else 'CKD'
        print(final)
        #print( f"{input_values} => {'No CKD' if model.predict([input_values])[0] else 'CKD'}")
        
    return render_template("result.html",final=final)

@app.route("/api/test")
def test_model_prediction():
    input_values = [55.0, 80.0, 1.020, 0.0, 0.0, 1, 1, 0, 0, 140.0, 49.0, 0.5, 150.0, 4.9, 15.7, 47.0, 6700.0, 4.9, 0, 0, 0, 0, 0, 0]
    return f"{input_values} => {'No CKD' if model.predict([input_values])[0] else 'CKD'}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
