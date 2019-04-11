import dataset

db = dataset.connect('sqlite:///database.db') # connect to SQLite database
table = db['emp_info'] # use 'emp_info' table in database

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    # find employee details by employee ID
    id_emp = input("[+] Enter employee ID : ")
    id_of_user = table.find_one(Employee_ID=id_emp) # list all users by ID
    print(id_of_user)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
