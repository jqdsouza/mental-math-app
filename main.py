from math_funcs import *
import time

if __name__ == "__main__":
	try: 
		lower_bound = int(input("Enter a lower bound integer: "))
		upper_bound = int(input("Enter an upper bound integer: "))
		num_seconds = int(input("Enter the length of time (in seconds) that you'd like to be tested for: "))
	except ValueError:
		print("Error: enter a number only.")
		raise

	try:
		operations = input("Select from the following operations: multiplication, addition, subtraction, division, exponentiation, perfect squares, square roots. Type 'all' if you'd like to be tested on every operation: ")
	except ValueError:
		print("Error: select only one of the following options")
		raise

	question_obj = QuestionGenerator(num_seconds, operations, lower_bound, upper_bound)
	start_time = time.time()
	print(start_time)
	
	while time.time() < start_time + num_seconds:
		question_obj.generate_question()

	print("Time's up. You got {x} questions correct out of {y} total questions".format(x = correct_count, y = total_question_count)) 
	
