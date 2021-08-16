import mysql.connector
myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="students"
)
myCursor = myDb.cursor()

print("*********STUDENT MANAGEMENT SYSTEM*********")


def select():
    print("Select Any One Of The Following Option \n1. CREATE STUDENT \n 2. READ STUDENT \n 3. UPDATE STUDENT \n 4. "
          "DELETE STUDENT \n 5. EXIT\n")
    selected = input("Enter Your Option: ")
    if selected == "1":
        name = input("Enter The Student Name: ")
        gender = input("Enter The Gender: ")
        age = input("Enter The Age: ")
        try:
            sql = "INSERT INTO students(NAME,GENDER,AGE) VALUES(%s,%s,%s)"
            val = (name, gender, age)
            myCursor.execute(sql, val)
            myDb.commit()
            print("\nStudent Created Successfully!\n")
        except:
            print("\nAn exception occurred\n")

        myDb.close()
        select()

    elif selected == "2":
        studentId = input("\nEnter The Student ID: ")
        try:
            sql = f"SELECT * FROM students WHERE ID = {studentId}"
            myCursor.execute(sql)
            myResult = myCursor.fetchone()
            print(myResult)
            myDb.commit()
        except:
            print("\nAn Exception occured!")
        myDb.close()
        select()
    elif selected == "3":
        studentId = input("Enter The Student Id To Update: ")
        name = input("Enter The name: ")
        age = input("Enter The age: ")
        try:
            sql = "UPDATE students SET NAME = %s, AGE = %s WHERE ID = %s"
            val = (name, age, studentId)
            myCursor.execute(sql, val)
            myDb.commit()
            print("\nStudent Updated Successfully!\n")
        except:
            print("\nAn Exception occured!")
        myDb.close()
        select()

    elif selected == "4":
        studentId = input("Enter The Student ID to DELETE: ")
        sql = f"DELETE FROM students WHERE ID = {studentId}"
        try:
            myCursor.execute(sql)
            myDb.commit()
            print("\nStudent Data deleted Successfully!")
        except:
            print("\nAn Exception occured!")

        myDb.close()
        select()
    else:
        exit()


select()

