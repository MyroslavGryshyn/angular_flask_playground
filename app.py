import os

from flask import Flask, json, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from cors_decorator import crossdomain

app = Flask(__name__, template_folder='templates')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import Location, Vacancy

db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/vacs', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def all():
    data_list = [i.serialize for i in Vacancy.query.all()[0:10]]
    return json.dumps(data_list)


@app.route('/api/vacs/<int:vacancy_id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def by_id(vacancy_id):
    return jsonify(Vacancy.query.get(vacancy_id).serialize)
