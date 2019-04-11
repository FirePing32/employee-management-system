import dataset

db = dataset.connect('sqlite:///database.db') # connect to SQLite database
table = db['emp_info'] # use 'emp_info' table in database

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    # find employee details by gender
    gender_emp_case = input("[+] Enter employee gender : ")
    gender_emp = gender_emp_case.lower() # remove regex errors
    gender_of_all_users = table.find_one(Gender=gender_emp) # list all users by gender
    print(gender_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
