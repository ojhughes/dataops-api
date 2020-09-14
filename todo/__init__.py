import os
from flask import Flask
from flask_cors import CORS

db_user = os.environ.get('POSTGRES_DB_USER')
db_psw = os.environ.get('POSTGRES_DB_PSW')
db_host = "dataops-bootcamp-postgresql" # Matches the kubernetes service name for postgresql
db_name = "learner"

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{0}:{1}@{2}/{3}'.format(
    db_user, db_psw, db_host, db_name
)
CORS(app, resources=r'/*', allow_headers="Content-Type")

import todo.views
