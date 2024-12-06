from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("danika.html")

@app.route("/heartfelt")
def heartfelt():
    return render_template("heartfelt.html")

if __name__ == "__main__":
    app.run(debug=True)
