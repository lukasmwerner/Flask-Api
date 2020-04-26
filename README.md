# Flask-Docs-Api
[Flask-Docs-Api | PyPI](https://pypi.org/project/Flask-Docs-Api)

A library to make doc generation painless

### Installation

```bash
pip install Flask-Docs-Api
```


### Sample Usage (copy & paste)

```python
from flask_api_docs.api import Api
api = Api(app, "Test")
api.route("/docs")
```
Sample
![](https://raw.githubusercontent.com/lwerner-lshigh/Flask-Api/master/sample.png)


### How it works
Flask-Docs-Api uses the docstrings of your existing python code and the methods defined in your routes to generate the api docs.


### Api of Flask-Docs-Api

Api class 

Constructor: Requires the app, and an optional name for the api docs title.

route: takes a url for the api doc route