# 2020.June.18-taskManager
Third Python capstone project - Basic user accessed task manager

Timeline :

Readme file planning 16-06-2020

Menu created 17-06-2020

Login function created 17-06-2020

register user function created 17-06-2020

username check function created 17-06-2020
	did not form part of initial planning
	function created to prevent duplication of code in login and register user functions

task check function created 18-06-2020
	did not form part of initial planning
	function created to prevent duplicate code in view_tasks, view_my_tasks and display_statistics functions

add task function created 18-06-2020

view tasks function created 18-06-2020

view my tasks function created 18-06-2020

display statistics function created 18-06-2020


Task : Note, task at hand to be extended upon within a later capstone project.

Part 1:

	Create a task manager program for a small business to keep track of assignments
	given to each worker, the date issued and date due, task description, and an
	indication if task is complete or not. Data stored/retrieved from file "tasks.txt".

	Program must allow users to login with a matching username/password combination
	that has been stored, and display an error message if username/password incorrect.
	Combinations stored and retrieved from file "user.txt".

	After login, menu of options must be displayed for user registration, add task,
	view all tasks, view tasks assigned to user specifically and exit. Each option must
	perform the function indicated by its name.

Part 2:

	Format the program to restrict menu options: only the username admin must be allowed
	to register users.
	Additionally, admin must have a new menu option to display statistics


Planning:

Functions:

	login:
	
		have user enter a username, then enter a password.
			check if username/password combination appears in "user.txt" file
			if both appear in combination continue to menu
			if one or both do not match, print error message
	
	register user:
		
		Only allow admin user to access this option
			use an if statement to check if user is admin upon login
			if result false, display error message if user attempts to add a new user
	
		prompt user for a new username, password and confirm password
			check that username doesn't exist already, print error message if it does
			check that password and confirmed password match, print error message if not
			write username/password combination to file "user.txt"
		
	add task:
	
		prompt user for username to which the task is assigned
			check that user exists within "user.txt" file
			if not, display error message and prompt again
		
		prompt user for task title
		
		prompt user for task description
		
		prompt user for task due date
		
		Write task to file "tasks.txt", defaulting completed to "No" and date assigned to current date
			import module datetime
			use input today = datetime.date.today()
				for formatting, use today.strftime(%x). output result will formatted to local version
				otherwise, use today.strftime(%d %b %Y) to output as dd mmm yyyy
	
	view all tasks
		
		display each task in an easy to ready format
	
	view my tasks
		
		display only tasks assigned to logged in user in an easy to read format
	
	display statistics
		
		only allow admin user to see and access this option
			use an if statement to check if user is admin upon login
			if result false, display error message if user attempts to display statistics
		
		when selected, option displays total number of tasks and total number of users
