from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://mongodb:27017/phonebook'

mongo = PyMongo(app)

@app.route('/phonebook', methods=['GET'])
def list():
  phones = mongo.db.phones
  result = []
  for i in phones.find():
    result.append({'name' : i['name'], 'phone' : i['phone']})
  return jsonify({'result' : result})

@app.route('/phonebook', methods=['POST'])
def add():
  phones = mongo.db.phones
  name = request.json['name']
  phone = request.json['phone']
  phones.insert({'name': name, 'phone': phone})
  return "Item added"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
