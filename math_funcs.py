import math
import time
import random

total_question_count = 0
correct_count = 0

class OperandGenerator:
    def __init__(self, num_operands, lower_bound = 2, upper_bound = 100):
        self.n = num_operands
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.operands = [random.randint(self.lower_bound, self.upper_bound) for i in range(num_operands)]

class BinaryOperation(OperandGenerator):
	def __init__(self, num1 = None, num2 = None):
		OperandGenerator.__init__(self, 2)
		self.num1, self.num2 = self.operands

	def addition(self):
		val = self.num1 + self.num2
		return val

	def subtraction(self):
		val = self.num1 - self.num2
		return val

	def multiplication(self):
		val = self.num1 * self.num2
		return val

	def division(self):
		val = self.num1 / self.num2
		return val

	def exponentiation(self):
		val = self.num1 ** self.num2
		return val

class UnaryOperation(OperandGenerator):
	def __init__(self, num1 = None):
		OperandGenerator.__init__(self, 1)
		self.num1 = self.operands

	def perfect_square(self):
		val = self.num1 ** 2
		return val

	def square_root(self):
		val = math.sqrt(self.num1)
		return val

class ValidateAnswer:
        def __init__(self, user_input, answer):
            self.user_input = user_input
            self.answer = answer

        def check_answer(self):
            output = 0
            if self.user_input == self.answer:
                output = 1
            else:
                output = 0

            return output

class QuestionGenerator(BinaryOperation, UnaryOperation, ValidateAnswer):
	operation_symbol_dict = {
		'addition' : '+', 
		'subtraction' : '-', 
		'multiplication' : 'x', 
		'division' : '/', 
		'exponentiation' : '^', 
		'square root' : 'Square root of ', 
		'perfect square' : 'Perfect square of '
		}

	def __init__(self, num_seconds, operation_type = [], lower_bound = 2, upper_bound= 100):
		self.num_seconds = num_seconds
		self.operation_type = operation_type
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
		operation_dict = {
			'addition' : super().addition(), 
			'subtraction' : super().subtraction(), 
			'multiplication' : super().multiplication(), 
			'exponentiation' : super().exponentiation(), 
			'division' : super().division(), 
			'square root' : super().square_root(), 
			'perfect square' : super().perfect_square()
		}
	
	def generate_question(self):
		print("self.operation_type[0]: ", self.operation_type)

		for operation in operation_dict.keys():
			print("operation: ", operation)
			symbol = operation_symbol_dict[operation]
			print("symbol: ", symbol)
			if operation in ['addition', 'subtraction', 'multiplication', 'division', 'exponentiation']:
				# print problem for user to compute
				binary_obj = BinaryOperation()
				operand1, operand2 = binary_obj.operands
				print("operand 1: ", operand1)
				print("operand 2: ", operand2)
				answer = operation_dict[operation]()

				try:
					user_input = int(input("{num_1} {symbol} {num_2}".format(num_1 = operand1, symbol = symbol, num_2 = operand2))) 
				
				except ValueError:
					print("Enter a number only.")
					continue

				# validate user answer
				checker = ValidateAnswer(user_input, answer)
				correct_count += checker.check_answer
		
			elif operation in ['square root', 'perfect square']:
				# print problem for user to compute
				unary_obj = UnaryOperation()
				operand1 = unary_obj.operands
				answer = operation_dict[operation]
                                        
				try:
					user_input = int(input("{symbol} {num_1}".format(symbol = symbol, num_1 = operand1)))
					total_question_count += 1

				except ValueError:
					print("Enter a number only.")
					continue

				# validate user answer
				checker = ValidateAnswer(user_input, answer)
				correct_count += checker.check_answer
				
				
				









