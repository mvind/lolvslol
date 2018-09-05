from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
CORS(app)

from app import routes
