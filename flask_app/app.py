from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the demo app running on :8080"

@app.route("/about")
def about():
    return "This is the about page!"

@app.route("/feature")
def feature():
    return "This is for the demo of the branch!"

if __name__ == "__main__":
    app.run("0.0.0.0", port = 8080, debug = True)
