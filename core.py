from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message" : "index"}

@app.route("/dashboard")
def dashboard():
    return {"message" : "dashboard"}

if __name__ == "__main__":
    app.run(debug = True)