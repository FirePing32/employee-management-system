import dataset

db = dataset.connect('sqlite:///database.db') # setup SQLite database
table = db['emp_info'] # setup table in database

user_name = "prakhar"
pass_word = "anonymous"

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! (Dev Mode) #")
print("--------------------------------------------------------")
print(" ")
print("[+] Enter database username and password - ")
print(" ")


def main_program():

    enter_username = input("[+] Enter username : ")
    enter_password = input("[+] Enter password : ")
    print(" ")
    print("-----------------")

    if enter_username == user_name and enter_password == pass_word: # successful login

        print(" ")
        print("[+] Login successful !")
        print("----------------------")
        print(" ")
        print(" ")

        def enter_employee_details(): # enter employee details

            emp_id = input("[+]Enter employee ID : ")
            name_case = input("[+] Enter employee name : ")
            age = input("[+] Enter employee age : ")
            gender_case = input("[+] Enter employee gender : ")

            name = name_case.lower() # saving it as lower() to make 
            gender = gender_case.lower() # it easy to search in database

            table.insert(dict(Employee_ID=emp_id, Name=name, Age=age, Gender=gender)) # saving to table 'emp_info' in database

            print(" ")
            print("[+] Saved to database !")
            print("-----------------------")
            print(" ")

            while True:
                enter_employee_details() # for continous input

        enter_employee_details()

    else:

        # null or incorrect input
        print(" ")
        print("[-] Incorrect username or password !")
        print("------------------------------------")
        print(" ")
        main_program()


main_program()
