from math_funcs.py import *
import time

if __name__ == "__main__":
	try: 
		lower_bound = int(input("Give a lower bound integer."))
		upper_bound = input("Give an upper bound integer.")
		num_seconds = input("Give the length of time (in seconds) that you'd like to be tested for.")
	except ValueError:
		print("Enter a number only.")

	try:
		operations = raw_input("Select from the following operations: multiplication, addition, subtraction, division, exponentiation, perfect squares, square roots. Type 'all' if you'd like to be tested on every operation.")
	except ValueError:
		print("Enter a string only.")

	question_obj = QuestionGenerator(operations, lower_bound, upper_bound, num_seconds)
	start_time = time.time()
	
	while (time.time() - start.time) < num_seconds:
		question_obj.generate_question()
	
