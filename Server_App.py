import dataset

db = dataset.connect('sqlite:///database.db')
table = db['emp_info']

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

    if enter_username == user_name and enter_password == pass_word:

        print(" ")
        print("[+] Login successful !")
        print("----------------------")
        print(" ")
        print(" ")

        def enter_employee_details():

            emp_id = input("[+]Enter employee ID : ")
            name_case = input("[+] Enter employee name : ")
            age = input("[+] Enter employee age : ")
            gender_case = input("[+] Enter employee gender : ")

            name = name_case.lower()
            gender = gender_case.lower()

            table.insert(dict(Employee_ID=emp_id, Name=name, Age=age, Gender=gender))

            print(" ")
            print("[+] Saved to database !")
            print("-----------------------")
            print(" ")

            while True:
                enter_employee_details()

        enter_employee_details()

    else:

        print(" ")
        print("[-] Incorrect username or password !")
        print("------------------------------------")
        print(" ")
        main_program()


main_program()
