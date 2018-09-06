import dataset

db = dataset.connect('sqlite:///database.db')
table = db['emp_info']

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    name_emp_case = input("[+] Enter employee name : ")
    name_emp = name_emp_case.lower()
    name_of_all_users = table.find_one(Name=name_emp)
    print(name_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
