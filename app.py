from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")


if __name__ == "__main__":
    app.run(debug=True)
