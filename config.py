from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["placement_db"]

users_collection = db["users"]
companies_collection = db["companies"]
applications_collection = db["applications"]
