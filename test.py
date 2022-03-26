import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['admin']

cars = db['pages_cars']


print(cars.find_one({'id':1})['tarihSaat'])
# cars = {
#         'tarihSaat': '', 
#         'Latitude': '', 
#         'Longitude': '',
#         'VehicleID': '', 
#         'id': '', 
#         'UserID': ''
#             }
#liste = list(cars.find())
# for item in cars.find():
#     print(item['UserID']
# 
# 


