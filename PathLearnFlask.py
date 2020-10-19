from flask import Flask, request, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pathlearn.thehomeserver.net'

app.config['MYSQL_HOST'] = 'pathlearn.thehomeserver.net'
app.config['MYSQL_USER'] = 'PathLearnTest'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route("/")
def index():
  return "Development Server"

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

@app.route('/add/<string:insert>')
def add(insert):
  cur = mysql.connection.cursor()
  cur.execute('''SELECT MAX(id) FROM users''')
  maxid = cur.fetchone()
  cur.execute('''INSERT INTO users (id, full_name) VALUES (%s, %s)''',(maxid[0] + 1, insert))
  mysql.connection.commit()
  return "Done"


if __name__ == '__main__':
    app.run(debug=True)