import dataset

db = dataset.connect('sqlite:///database.db')
table = db['emp_info']

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    gender_emp_case = input("[+] Enter employee gender : ")
    gender_emp = gender_emp_case.lower()
    gender_of_all_users = table.find_one(Gender=gender_emp)
    print(gender_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
