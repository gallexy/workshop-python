from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a=10
    b=a+5
    return "Hello, Python!"


if __name__ == "__main__":
    app.run()

