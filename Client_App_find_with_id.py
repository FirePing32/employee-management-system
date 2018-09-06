import dataset

db = dataset.connect('sqlite:///database.db')
table = db['emp_info']

print(" ")
print("# Welcome to Zinderbot Alpha program v1.0 ! #")
print("---------------------------------------------")
print(" ")


def main_program():

    id_emp = input("[+] Enter employee ID : ")
    id_of_user = table.find_one(Employee_ID=id_emp)
    print(id_of_user)
    print("---------------------------------------------")
    print(" ")


while True:
    main_program()
