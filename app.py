from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList

# logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vivek'
api = Api(app)
# app.logger.info("Flask logger ready!")

@app.before_first_request()
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

# items = []

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')

# stores = [
#     {
#         'name':'My wonderful store',
#         'items': [
#             {
#                 'name':'My Item',
#                 'price': 15.99
#             }
#         ]
#     }
# ]
#
# # POST /store data: {name:}
# @app.route('/store', methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'item':[]
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
#
# # GET /store/<string:name>
# @app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some_name
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#     return jsonify({'message':'store not found'})
#
#
# # GET /store
# @app.route('/store')
# def get_stores():
#     return jsonify({'stores':stores})
#
# # POST /store/<string:name>/item {item:, price:}
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify(new_item)
#     return jsonify({'message':'store not found'})
#
# # GET /store/<string:name>/item
# @app.route('/store/<string:name>/item')
# def get_items_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items':store['items']})
#     return jsonify({'message':'store not found'})
#
# @app.route('/')
# def home():
#     return "Hello World"

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)