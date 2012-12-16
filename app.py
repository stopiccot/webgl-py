from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello <i>World</i> from <b>Flask</b>!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')