from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

from YouTubeSearch import getTop5Videos

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'pathlearn.thehomeserver.net'
app.config['MYSQL_USER'] = 'PathLearnTest'
app.config['MYSQL_PASSWORD'] = 'testpass'
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/')
def index():
	return 'Hello tp PathLearn Flask API services!'


@app.route("/api/userData", methods=['POST'])
def firebase():
    userDetails = {
        'idToken': request.json['idToken'],
        'email': request.json['email'],
        'password': request.json['password'],
        'phone': request.json['phone'],
        'refreshToken': request.json['refreshToken'],
        'expiresIn': request.json['expiresIn'],
        'localId': request.json['localId'],
        'firstName': request.json['firstName'],
        'lastName': request.json['lastName'],
        'kind': request.json['kind'],  
    }
    return jsonify({'userDetails': userDetails})

@app.route("/api/test", methods=['POST'])
def test():
    token = {
        'email': request.json['email'],
        'password': request.json['password'],
    }
    return jsonify({'token': token})

@app.route("/api/youtube/<searchterm>", methods=['GET'])
def youtube(searchterm):
    return getTop5Videos(searchterm)
    
if __name__ == '__main__':
	app.run(debug=True)
