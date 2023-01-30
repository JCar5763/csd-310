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

# first print statement
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# formatting information with loop
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# creating the test document 
test_doc = {
    "student_id": "1010",
    "first_name": "Jacob",
    "last_name": "Doe"
}

# inserting the test document 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert print statements 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# find () call for the new student document
student_test_doc = students.find_one({"student_id": "1010"})

# secondary print statements - results
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# delete_one () method call
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find () call for all students 
new_student_list = students.find({})

# Print statements again - display
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# formatting info with a loop 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
# print exit statement
input("\n\n  End of program, press any key to continue...")