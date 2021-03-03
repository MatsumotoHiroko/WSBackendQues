from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

mongo_username = 'user-backend'
mongo_password = 'Y9qPwZwpkNpPjmaj'
db_name = ""

DB_URI = f"mongodb://{mongo_username}:{mongo_password}@clusterrestapitest-shard-00-00.ehwyd.mongodb.net:27017,clusterrestapitest-shard-00-01.ehwyd.mongodb.net:27017,clusterrestapitest-shard-00-02.ehwyd.mongodb.net:27017/{db_name}?ssl=true&replicaSet=ClusterRESTApiTest-shard-0&authSource=admin&retryWrites=true&w=majority"
app.config['MONGODB_HOST'] = DB_URI

# write your code here