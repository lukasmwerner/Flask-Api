
import flask
from flask import Flask


app = Flask(__name__)
from flask_api_docs.api import Api
api = Api(app, "/docs", globals(), "Test" )

@app.route("/")
def testApp():
    '''Returns 'hello World!' '''
    return "hello World!"

if __name__ == "__main__":
    app.run()