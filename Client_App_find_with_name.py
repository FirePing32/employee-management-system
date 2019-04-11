import dataset

db = dataset.connect('sqlite:///database.db') # connect to SQLite database
table = db['emp_info'] # use 'emp_info' table in database

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    # find employee details by name
    name_emp_case = input("[+] Enter employee name : ")
    name_emp = name_emp_case.lower() # remove regex errors
    name_of_all_users = table.find_one(Name=name_emp) # list all users by name
    print(name_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
