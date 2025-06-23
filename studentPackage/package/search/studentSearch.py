
def search(data):
    
    
    # pass

    while True:
        print("Press 1 for search by ID: ")
        print("Press 2 for search by Name: ")
        print("Press 3 for search by Qualification: ")
        print("Press 4 for exit: ")

        choice = input("Enter any number: ")
        
        if int(choice) == 1 and choice.isdigit:
            student_id = int(input("Enter student ID: "))
            
            for dic in data:
                if dic["id"] == student_id:
                    print(dic)
                    
                    break
                else:   
                    print("Invalid entry!! Try again")
        
        elif int(choice) == 2 and choice.isdigit():

            name = input("Enter student name: ").lower()
            

            for dic in data:
                if dic["name"].lower() == name:
                    print(dic)
                    
                    break

                else:   
                    print("Invalid entry!! Try again")

        elif int(choice) == 3 and choice.isdigit():

            qualification = input("Enter student qualification: ").lower()
            

            for dic in data:
                if dic["qualification"] == qualification:
                    print(dic)
                    
                else:   
                    print("Invalid entry!! Try again")

        elif int(choice) == 4 and choice.isdigit():
            break

        else:
            print("*"*50)
            print("\tSelect from above options!!")
            print("*"*50)
