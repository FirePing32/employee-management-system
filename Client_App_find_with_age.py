import dataset

db = dataset.connect('sqlite:///database.db') # connect to SQLite database
table = db['emp_info'] # use 'emp_info' table in database

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    # find employee details by age
    age_emp = input("[+] Enter employee age : ")
    age_of_all_users = table.find_one(Age=age_emp) # list all users by age
    print(age_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
