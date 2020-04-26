
import flask
from flask import Flask
from flask_docs_api.api import Api

app = Flask(__name__)
api = Api(app, "Test")
api.route("/docs")


@app.route("/")
def testApp():
    '''Returns 'hello World!' '''
    return "hello World!"

if __name__ == "__main__":
    app.run()