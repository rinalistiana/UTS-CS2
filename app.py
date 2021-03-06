from flask_restful import Resource, Api
from flask import Flask, Response, json, jsonify, request, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

#Rina Listiana 18090090

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/kampus'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(10), unique=True)
    nama = db.Column(db.String(100))
    alamat= db.Column(db.String(120))

    def __init__(self, nim, nama, alamat):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat

    @staticmethod
    def get_all_users():
        return Mahasiswa.query.all()

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nim', 'nama', 'alamat')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/mahasiswa', methods=['POST'])
def add_user():
    mahasiswa = Mahasiswa.query.get(id)
    
    nim = request.json['nim']
    nama = request.json['nama']
    alamat = request.json['alamat']

    mahasiswa.nim = nim
    mahasiswa.nama = nama
    mahasiswa.alamat = alamat

    db.session.add(mahasiswa)
    db.session.commit()

    result = user_schema.dump(mahasiswa)
    return jsonify(result)

@app.route('/mahasiswa', methods=['GET'])
def get_users():
    all_users = Mahasiswa.get_all_users()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_user(id):
    mahasiswa = Mahasiswa.query.get(id)
    return user_schema.jsonify(mahasiswa)

@app.route('/mahasiswa/<int:id>', methods=['POST'])
def add_user(id):
    mahasiswa = Mahasiswa.query.get(id)

    nim = request.json['nim']
    nama = request.json['nama']
    alamat = request.json['alamat']

    mahasiswa.nim = nim
    mahasiswa.nama = nama
    mahasiswa.alamat = alamat

    db.session.add(mahasiswa)
    db.session.commit()

    result = user_schema.dump(mahasiswa)
    return jsonify(result)

@app.route('/mahasiswa/<int:id>', methods=['PUT'])
def update_user(id):
  mahasiswa = Mahasiswa.query.get(id)

  nim = request.json['nim']
  nama = request.json['nama']
  alamat = request.json['alamat']

  mahasiswa.nim = nim
  mahasiswa.nama = nama
  mahasiswa.alamat = alamat

  db.session.commit()
  result = user_schema.dump(mahasiswa)
  return jsonify(result)

@app.route('/mahasiswa/<int:id>', methods=['DELETE'])
def delete_product(id):
  mahasiswa = Mahasiswa.query.get(id)
  db.session.delete(mahasiswa)
  db.session.commit()

  return jsonify()

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/getUser', methods=['GET'])
@jwt_required
def getuser():
    all_users = Mhs.get_all_users()
    result = users_schema.dump(all_users)
    return jsonify(result), 200
    # return jsonify(Mhs.query.all()), 200


if __name__ == '__main__':
    app.run()
