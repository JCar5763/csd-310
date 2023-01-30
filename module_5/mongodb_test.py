#import MongoClient
from pymongo import MongoClient

# MongoDB connection string copied value
url = "mongodb+srv://admin:admin@cluster0.k59uwfs.mongodb.net/?retryWrites=true&w=majority"

# call the MongoClient
client = MongoClient(url)

# assign to pytech database
db = client.pytech

# Connected collections and print statement 
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# print the exit message
input("\n\n  End of program, press any key to exit... ")