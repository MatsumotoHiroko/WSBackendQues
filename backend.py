from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
from wtforms import validators
import datetime

app = Flask(__name__)

mongo_username = 'user-backend'
mongo_password = 'Y9qPwZwpkNpPjmaj'
db_name = "Test"

DB_URI = f"mongodb://{mongo_username}:{mongo_password}@clusterrestapitest-shard-00-00.ehwyd.mongodb.net:27017,clusterrestapitest-shard-00-01.ehwyd.mongodb.net:27017,clusterrestapitest-shard-00-02.ehwyd.mongodb.net:27017/{db_name}?ssl=true&replicaSet=ClusterRESTApiTest-shard-0&authSource=admin&retryWrites=true&w=majority"
app.config['MONGODB_HOST'] = DB_URI

# write your code here
db = MongoEngine(app)

class Person(db.EmbeddedDocument):
    name = db.StringField(required=True)
    gender = db.StringField(required=True)
    occupation = db.StringField(required=True)
    annualIncome = db.IntField(required=True)
    year_of_birth = db.StringField(required=True)

class Couple(db.Document):
    couple_id = db.IntField(required=True)
    maritalStatus = db.StringField(required=True)
    person = db.EmbeddedDocumentListField(Person)

now = datetime.datetime.now()

@app.route('/couples')
def index():
  couples = Couple.objects
  print(couples)

  return jsonify(couples), 200


# o Marital status = Married 
# o Both are older than 23 years old 
# o At least 1 spouse is a Student 
@app.route('/couples/young')
def index():
  couples = Couple.objects(maritalStatus='Married')
  result = []
  

  for couple in couples:
      for person in couple.person:
          if person.occupation != 'Student':
              continue
        
          if now.year - int(person.year_of_birth) <= 23:
              continue
      
          result.append
        
        
  result = {
        
    }

  return jsonify(couples), 200

@app.route('/couples', methods=['POST'])
def create_item():
    json_data = request.json
    
    persons = []
    for p_json_data in json_data['person']:
        person = Person(name=p_json_data['name'], gender=p_json_data['gender'], occupation=p_json_data['occupation'], 
        annualIncome=p_json_data['annualIncome'], year_of_birth=p_json_data['year_of_birth'])
        persons.append(person)
    couple = Couple(couple_id=json_data['couple_id'], maritalStatus=json_data['maritalStatus'], person=persons)
    couple.save()
    result = {
        'message': 'create successful',
        'couple': couple,
        'persons': persons,
    }
    return jsonify(result), 201

@app.route('/couple/<int:couple_id>', methods=['DELETE'])
def delete_item(couple_id): 
    Couple.objects(couple_id=couple_id).first().delete()
    result = {
        'message': 'delete successful',
        'couple_id': couple_id
    }
    return jsonify(result), 200

# @app.route('/user/<int:id>', methods=['GET'])
# def get_item(id):
#     result = {
#         'id': id
#     }
#     return jsonify(result), 200



# @app.route('/user/<user_id>', methods=['PATCH'])
# def update_item(user_id):
#     user = User.objects(user_id=user_id).first()
#     json_data = request.json
#     user.email = json_data['email']
#     user.first_name = json_data['first_name']
#     user.last_name = json_data['last_name']
#     user.save()
#     result = {
#         'message': 'update successful',
#         'user': user
#     }
#     return jsonify(result), 200