from pymongo import MongoClient

# MongoDB connection string copied value
url = "mongodb+srv://admin:admin@cluster0.k59uwfs.mongodb.net/?retryWrites=true&w=majority"

# call the MongoClient
client = MongoClient(url)

# assign to pytech database
db = client.pytech

# students collection 
students = db.students

# find () call for all students 
student_list = students.find({})

# initial print statement
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# formatting info with loop 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
# updating student_id 1007 - Benny Bopt student
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bopt"}})

# find () for the Benny Bopt document 
benny = students.find_one({"student_id": "1007"})

# Secondary print statement
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# print the updated Benny Bopt document
print("  Student ID: " + benny["student_id"] + "\n  First Name: " + benny["first_name"] + "\n  Last Name: " + benny["last_name"] + "\n")

# exit print statement 
input("\n\n  End of program, press any key to continue...")