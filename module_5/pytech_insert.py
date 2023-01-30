#import MongoClient
from pymongo import MongoClient

# MongoDB connection string copied value
url = "mongodb+srv://admin:admin@cluster0.k59uwfs.mongodb.net/?retryWrites=true&w=majority"

# call the MongoClient
client = MongoClient(url)

# assign to pytech database
db = client.pytech

# add Theo document with insert_one () information
theo = {
    "student_id": "1008",
    "first_name": "Theo",
    "last_name": "Scouts",
    }

# add Benny document with insert_one () information
benny = {
    "student_id": "1007",
    "first_name": "Benny",
    "last_name": "Bopt",
    }

# add Fred document with insert_one () information
fred = {
    "student_id": "1009",
    "first_name": "Fred",
    "last_name": "Junior",
    }

# Students collection 
students = db.students

# Print statements, ending, and insert_one call
print("\n  -- INSERT STATEMENTS --")
theo_student_id = students.insert_one(theo).inserted_id
print("  Inserted student record Theo Scouts into the students collection with document_id " + str(theo_student_id))

benny_student_id = students.insert_one(benny).inserted_id
print("  Inserted student record Benny Bopt into the students collection with document_id " + str(benny_student_id))

fred_student_id = students.insert_one(fred).inserted_id
print("  Inserted student record Fred Junior into the students collection with document_id " + str(fred_student_id))

input("\n\n  End of program, press any key to exit... ")