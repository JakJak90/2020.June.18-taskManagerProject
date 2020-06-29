#Program for managing tasks assigned to users, which writes to and reads tasks and users
#from the "tasks.txt" and "user.txt" files respectively

#Import required module

import datetime

#Define required functions

#Function to create dictionary of username/password combinations

def username_check() :

    #Declare local variables
    
    users = {}

    #Access "user.txt" file in read mode
    
    with open("user.txt", "r") as f :

        #Run through "user.txt" file to check for matching combination
        
        for line in f :

            user_check = line.strip("\n")
            
            #Prevent range out of bound errors as caused by empty lines
            
            if user_check != "" :
                user_check = user_check.split(", ")
                users.update({user_check[0]: user_check[1]})

    return users

#Function to create a list of tasks

def task_check() :

    #Declare local variables
    
    tasks = []

    #Access "tasks.txt" file in read mode
    
    with open("tasks.txt", "r") as f :

        #Run through "tasks.txt" file to check for matching combination
        
        for line in f :

            task_check = line.strip("\n")
            
            #Prevent range out of bound errors as caused by empty lines
            
            if task_check != "" :
                task_check = [task_check.split(", ")]
                tasks.extend(task_check)

    return tasks
            

#Function to log onto task manager program by matching username/password combination

def login() :  

    #Get username and password combination from user
        
    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")
    print()

    #Call username_check() function to compare login details to dictionary storage

    user_list = username_check()
    

        
    if username in user_list and user_list.get(username) == password :
        return username

    else :
        print("Your username and/or password is incorrect, please ensure your caps lock is off and try again.\n")
        return "loop"
            
#Function to display appropriate menu

def menu() :

    #Declare local variables

    carry_on = True

    #While loop to continue returning to menu until user selects exit

    while carry_on :
        print("Please select one of the following options:\n")
        print("r\t- register user\n")
        print("a\t- add task\n")
        print("va\t- view all tasks\n")
        print("vm\t- view my tasks\n")
        
        #Only show the display statistics option if admin is logged in
        if admin_rights :
            print("d\t- display statistics\n")
        
        print("e\t- exit")
        print()
        selection = input()
        print()

        #if-elif-else statement to call appropriate function based on menu selection
        
        if selection.lower() == "r" :
            register_user()
            
        elif selection.lower() == "a" :
            add_task()
            
        elif selection.lower() == "va" :
            view_tasks()
            
        elif selection.lower() == "vm" :
            view_my_tasks()
            
        elif selection.lower() == "d" :
            display_statistics()
            
        elif selection.lower() == "e" :
            carry_on = False
            
        else :
            print("Your selection did not meet a menu item. Please try again.\n")

#Function to register a new user to "user.txt" file
            
def register_user() :

    #Declare local variables

    carry_on = True

    user_list = username_check()

    #check that user has admin rights

    if admin_rights == False :
        print("You do not have permission to perform this action.\n")

    else :

        #While loop to ensure correct details are added

        while (carry_on) :

            #Access "user.txt" file in append mode
        
            with open("user.txt", "a") as f :

                #Get username to be added from admin
            
                new_username = input("Please enter the username you would like to add, or 'e' to exit:\n")
                print()

                #check that username does not exist

                if new_username in user_list :
                    print("That username is already taken, please try a different username.\n")

                else :
                    password = input(f"Please enter a password for {new_username}:\n")
                    print()
                    confirmation = input("Please confirm the password entered:\n")

                    if password == confirmation :
                        f.write(f"\n{new_username}, {password}\n")
                        print(f"new user {new_username} has been added!")
                        print()
                        carry_on = False

                    else :
                        print("Your password and confirmation do not match, please try again.\n")


#Function to add a task to "tasks.txt" file

def add_task() :

    #Declare local variables

    on_user_list = True

    #Call user_check for validation

    users_list = username_check()

    #Access the "tasks.txt" file in append mode
    
    with open("tasks.txt", "a") as f :
        
        #Get task information from user
        while (on_user_list) :
            asigned_user = input("Who is the owner for this task?\n")

        #Ensure that assigned user is in the "user.txt" file
            if asigned_user in users_list :
                on_user_list = False
            else :
                print("The given user does not exist, please try again.\n")
            
        title = input("What is the task title?\n")
        description = input("Please enter a description of the task:\n")

        #Determine assigned date from local time
        
        today = datetime.date.today()

        #Format date to be in dd mmm yyyy format
        
        today = today.strftime("%d %b %Y")
        
        date_due = input("Please enter when the task is due in dd mmm yyyy format:\n")
        complete = "No"

        f.write(f"\n{asigned_user}, {title}, {description}, {today}, {date_due}, {complete}\n")
        

#Function to view all tasks within the "tasks.txt" file

def view_tasks() :
    
    #Get list of registered tasks
    
    tasks = task_check()
    
    #Loop through each tasks to print them
    
    for i in range(0, len(tasks)) :
        
        #Break task down into assignable pieces
        
        asigned_user = tasks[i][0]
        title = tasks[i][1]
        description = tasks[i][2]
        date_assigned = tasks[i][3]
        date_due = tasks[i][4]
        complete = tasks[i][5]
        
        #Print task in a user friendly manner
        
        print("-"*50)
        print(f"Task:\t\t\t{title}")
        print(f"Assigned to:\t\t{asigned_user}")
        print(f"Date assigned:\t\t{date_assigned}")
        print(f"Due date:\t\t{date_due}")
        print(f"Task complete?\t\t{complete}")
        print(f"Task description:\n{description}")
    
    print("-"*50)
    print()
            
        

#Function to view all tasks assigned to the logged in user within the "tasks.txt" file

def view_my_tasks() :
    
    #Get list of registered tasks
    
    tasks = task_check()
    
    #Loop through each tasks to print them
    
    for i in range(0, len(tasks)) :
        
        #Break task down into assignable pieces
        
        asigned_user = tasks[i][0]
        title = tasks[i][1]
        description = tasks[i][2]
        date_assigned = tasks[i][3]
        date_due = tasks[i][4]
        complete = tasks[i][5]
        
        #If user and assigned_user are the same, print task in a user friendly manner
        if user == asigned_user :
            print("-"*50)
            print(f"Task:\t\t\t{title}")
            print(f"Assigned to:\t\t{asigned_user}")
            print(f"Date assigned:\t\t{date_assigned}")
            print(f"Due date:\t\t{date_due}")
            print(f"Task complete?\t\t{complete}")
            print(f"Task description:\n{description}")
    
    print("-"*50)
    print()

#Function to display a count of all tasks and all users contained within "user.txt" and "tasks.txt" files

def display_statistics() :
    
    #Declare local variables
    
    outstanding_tasks = 0

    #Error message if none admin user enters "d" as a menu option
    
    if admin_rights == False :
        print("Your selection did not meet a menu item. Please try again.\n")
        return
    
    #Get count of users
    
    users = username_check()
    user_count = len(users.keys())
    
    print(f"The total number of registered users is {user_count}.")
    
    #Get count of registered tasks 
    
    tasks = task_check()
    task_count = len(tasks)
    
    #Check how many are still outstanding
    
    for i in range(0, task_count) :
        if tasks[i][5].lower() == "no" :
            outstanding_tasks += 1
            
    print(f"The total number of registered tasks is {task_count}, of which {outstanding_tasks} are still outstanding.")
    print()

#Declare gloabl variables

login_attempt = True
admin_rights = False

#Main program

#Loop to log onto task manager program
#If admin logs on, assign admin rights

while (login_attempt) :
    user = login()

    if user == "admin" :
        admin_rights = True
        login_attempt = False

    elif user != "loop" :
        login_attempt = False

menu()


