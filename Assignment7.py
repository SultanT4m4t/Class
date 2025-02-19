# Assignment7

main_dict = {'1':{'name':'Andrew', 'age':32, 'grade':90}, 
             '2':{'name':'Mo', 'age':43, 'grade':90}
             } 
while True:
    choice = input('Enter choice: ')
    if choice == '1':
        std_id = input('Enter student ID: ')
        std_name = input('Enter name of student: ')
        std_age = int(input('Enter age of student: '))
        std_grade = int((input('Enter grade of student: ')))
        std_dict = {
        'name': std_name,
        'age': std_age,
        'grade': std_grade 
}
        main_dict[std_id] = std_dict
        print(main_dict[std_id]['name'], "added successfully")

    #viewing a particular student
    elif choice == '2':
        view_choice = input('View details by name or student ID: ')
        view_choice_upper = view_choice.upper()

        #Viewing by ID
        if view_choice_upper == 'ID':
            view_id = input('Enter ID of student: ')
            print(str(view_id)+'.', main_dict[view_id])

         #Viewing by name   
        elif view_choice_upper == 'NAME':
            view_name = input('Enter name of student you want to view: ')
            for names in main_dict.values():
                if view_name in names['name']:
                    print(names['name'], 'found\n',names)
                    break
            #If student is not found
            else:
                print('Name not found')
        #ifUser doesn't enter 'name' or 'ID'
        else:
            print('I SAID TYPE NAME OR ID!!!!')

     #Viewing all students   
    elif choice == '3':
        print('ID    NAME          AGE     GRADE')
        for view_keys, view_values in main_dict.items():
            print(f"{view_keys}     {view_values['name'] + ' '*(7-len(view_values['name']))}       {str(view_values['age']) + ' '*(3-len(str(view_values['age'])))}     {view_values['grade']}")

    #Updating a student's details
    elif choice == '4':
        update = input('Enter ID of student: ')
        if update in main_dict:
            ukey = input('Enter info you want to update: ')
            if ukey in main_dict[update]:
                new_value = input('Enter new value: ')
                main_dict[update][ukey] = new_value 
                print(main_dict[update]) 
            else:
                print('Info you want to update doesnt exist')         
            
        else:
            print('Student ID not correct')

    elif choice == '5':
        grade_total = 0
        for graded in main_dict.values():
            grade_num = graded['grade']
            grade_total = grade_total + grade_num
        grade_avg = grade_total/len(main_dict)
        print(f'{grade_avg:.2f}')

    elif choice == '6':
        print("Goodbye")
        break

    else:
        print('Invalid choice')