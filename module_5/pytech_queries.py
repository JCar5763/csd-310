#import MongoClient
from pymongo import MongoClient

# MongoDB connection string copied value
url = "mongodb+srv://admin:admin@cluster0.k59uwfs.mongodb.net/?retryWrites=true&w=majority"

# call the MongoClient
client = MongoClient(url)

# assign to pytech database
db = client.pytech

#  students collection
students = db.students

# find () call to find the information on the students
student_list = students.find({})

# initial print statement
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Formatting the information from the documents
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
# call theo document specifically with find_one ()
theo = students.find_one({"student_id": "1008"})

#  Printing info for theo separately
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + theo["student_id"] + "\n  First Name: " + theo["first_name"] + "\n  Last Name: " + theo["last_name"] + "\n")

# print exit statement
input("\n\n  End of program, press any key to continue...")
