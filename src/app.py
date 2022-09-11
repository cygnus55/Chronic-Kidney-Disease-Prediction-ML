import os
import pickle

import sklearn

from flask import Flask, render_template
from forms import SubmissionForm


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    form = SubmissionForm()
    return render_template("index.html", form=form)


@app.route("/api/test")
def test_model_prediction():
    with open("../models/dt_model.pkl", "rb") as f:
        model = pickle.load(f)
    input_values = [55.0, 80.0, 1.020, 0.0, 0.0, 1, 1, 0, 0, 140.0, 49.0, 0.5, 150.0, 4.9, 15.7, 47.0, 6700.0, 4.9, 0, 0, 0, 0, 0, 0]
    return f"{input_values} => {'No CKD' if model.predict([input_values])[0] else 'CKD'}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
