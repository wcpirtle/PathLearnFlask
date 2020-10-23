from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'pathlearn.thehomeserver.net'
app.config['MYSQL_USER'] = 'PathLearnTest'
app.config['MYSQL_PASSWORD'] = 'testpass'
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route("/api/firebase", methods=['POST'])
def firebase():
    token = {
        'email': request.json['email'],
        'expiresIn': request.json['expiresIn'],
        'idToken': request.json['idToken'],
        'kind': request.json['kind'],
        'localId': request.json['localId'],
        'refreshToken': request.json['refreshToken']
    }
    return jsonify({'token': token})