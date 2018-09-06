import dataset

db = dataset.connect('sqlite:///database.db')
table = db['emp_info']

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    age_emp = input("[+] Enter employee age : ")
    age_of_all_users = table.find_one(Age=age_emp)
    print(age_of_all_users)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
