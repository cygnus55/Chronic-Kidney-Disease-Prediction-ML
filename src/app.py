import os

from flask import Flask, render_template
from forms import SubmissionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    form = SubmissionForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
