from flask import Flask

app = Flask(__name__, template_folder='template')


@app.route("/")
def index():
    return b'<h2>You have reached the Intersection Trivia API!</h2>'


if __name__ == "__main__":
    app.run()
