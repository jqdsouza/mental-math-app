import math
import time
import random

class OperandGenerator:
        def __init__(self, num_operands, lower_bound = 2, upper_bound = 100):
                self.n = num_operands
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
                self.operands = [random.randint(self.lower_bound, self.upper_bound) for i in range(num_operands-1)]

class BinaryOperation(OperandGenerator):
	def __init__(self):
		OperandGenerator.__init__(self, 2)

	def addition(self):
		num1, num2 = self.operands
		val = num1 + num2
		return val

	def subtraction(self):
		num1, num2 = self.operands
		val = num1 - num2
		return val

	def multiplication(self):
		num1, num2 = self.operands
		val = num1 * num2
		return val

	def division(self):
		num1, num2 = self.operands
		val = num1 / num2
		return val

	def exponentiation(self):
		num1, num2 = self.operands
		val = num1 ** num2
		return val

class UnaryOperation(OperandGenerator):
	def __init__(self):
		OperandGenerator.__init__(self, 1)

	def perfect_square(self):
      		num1  = self.operands
                val = num1 ** 2
                return val

	def square_root(self):
		num1 = self.operands
                val = math.sqrt(num1)
                return val

class ValidAnswer:
        def __init__(self, user_input, answer):
                self.user_input = user_input
                self.answer = answer

        def check_answer(self):
                output = ""
                if self.user_input == self.answer:
                        output = "Correct!"
                else:
                        output = "Incorrect, try again."

                return output

class QuestionGenerator(BinaryOperation, UnaryOperation, ValidAnswer):
	operation_dict = {'addition' : addition, 'subtraction' : subtraction, 'multiplication' : multiplication, 
		'division' : division, 'square root' : square_root, 'perfect square' : perfect_square}

	def __init__(self, operation_type = ['addition'], num_seconds):
		self.operation = operation_dict[operation_type]
		self.num_seconds = num_seconds
	
	def generate_question(self):
		if len(self.operation_type) < 1:
			print("Please input an operation you'd like to be tested on.")
		
		if self.operation_type[0] == 'all':
			for operation in operation_dict.keys():
				answer = operation_dict[operation]()
