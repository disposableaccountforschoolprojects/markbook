#Importing string for isalpha list
import string

#The range of scores possible
MIN_SCORE = 0
MAX_SCORE = 100

#the possible grades
GRADE_NA = 0
GRADE_A = 50
GRADE_M = 70
GRADE_E = 90

#list of student scores
student_scores = [ 

]

def print_error(error_msg):
	'''formant and prints a error message'''
	print(f"ERROR: {error_msg}")

def get_student_score():
	'''Gets the student score and makes sure it's valid'''
	valid_data = False
	#repeats until a valid data is given
	while not valid_data:	
		#check for errors
		try:
			#collects the score
			score = int(input(f"Input your score ({MIN_SCORE} to {MAX_SCORE}): "))
			#checks the if the score is in range then ends the loop if it is
			#or else prints an error message
			if score in range(MIN_SCORE,MAX_SCORE):
				valid_data = True
				print("Score successfully added")
			else:
				print_error(f"Score must be between ({MIN_SCORE} to {MAX_SCORE})")
		except:
			# if the user inputed non number characters it would error out
			# and ask the user to reinput
			print_error("Please only input numbers")
	#retuns the score which has been validated
	return score

def get_student_name():
	'''Gets the students name and checks if it's valid'''
	valid_data = False
	#repeats until a valid data is given
	while not valid_data:	
		#collects user name
		name = input(f"Input your name: ")
		#strips the name of any spaces
		name = name.strip()
		#checks if name only has characters
		if name.isalpha():
			#checks if name is blank
			if not name == "":
				#exits the loop if all checks clear
				valid_data = True
				print("Name successfully added")
			else:
				#errors out if name is blank
				print_error(f"Name can't be blank")
		else:
			print_error(f"Name can only have letters")
	#title case the name and returns it
	name = name.title()
	return name


def add_student():
	'''adds students to the list with their grades'''
	#gets students scores and names
	s_score = get_student_score()
	s_name = get_student_name()

print(get_student_score())
print(get_student_name())
