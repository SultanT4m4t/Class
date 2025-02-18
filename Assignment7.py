#Assignment7

print('Hey There! Choose an action')
std_list = [{'name':'And', 'age':32, 'grade': 95},{'name':'Mo', 'age':32, 'grade': 100}]
num_2 = []
def add_std():
    std_name = input('Enter your name: ')
    std_age = int(input('Enter your age: '))
    std_grade = int(input('Enter your grade: '))       
    std_dict = {
            'name':std_name,
            'age':std_age,
            'grade':std_grade
        }
    std_list.append(std_dict)
    print(std_name, 'added succesfully')

def view_std():
    print(f'You have {len(std_list)} students(s) in your student list')
    for std_view in std_list:
        print(f'{std_view['name']}')

def update_std():
    for a in std_list:
            # print(a)
            update_value = input('Enter whose info you want to update: ')
            if update_value in a.values():
                update_key = input('Enter the info you want to update: ')
                if update_key in a.keys():
                    new_update = input('Enter the new value: ')
                    a.update({update_key:new_update})
                    print(f'{update_key} succesfully changed to {new_update}')
                    break
            
                else:
                    print('info does not exist: ')
                    break

def std_details():
    for b in std_list:
            for c,d in b.items():
                print(f'{c}:{d}')

def avg():
    sum_num = 0
    for num in std_list:
        num_1 = (num['grade'])
        num_2.append(num_1)
    for nums in num_2:
        sum_num = sum_num + nums
    avg_num = sum_num/len(num_2)
    print(f'The average grade is {avg_num}')
    return avg_num
    
        

            

def exit():
    print('Goodbye')

while True:
    print('1. Add a student\n2. View students\n3. Update student records\n4. View students\n5. Calculate average\n6. Exit program')
    choice = input('Enter your choice: ')

    #Adding a student
    if choice == '1': 
        add_std()

    #Viewing students
    elif choice == '2':
        view_std()

    #Updating friend's info
    elif choice == '3':
        update_std()
                
    #View friend details
    elif choice == '4':
        std_details()

    elif choice == '5':
        avg()

    #Exit program
    elif choice == '6':
        exit()
        break
    else:
        print('Invalid choice')