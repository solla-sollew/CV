
# A very simple Flask CV with Azure...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/resume")
def indexresume():
    return render_template("indexUC.html")

@app.route("/")
def indexcv():
    return render_template("index.html")

