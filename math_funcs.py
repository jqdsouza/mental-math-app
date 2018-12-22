import math
import time
import random

class RandomNumGen:
        def __init__(self, lower_bound, upper_bound, operands):
                self.n = num_operands
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
                self.operands = [random.randint(self.lower_bound, self.upper_bound) for i in range(n-1)]

        def generate_questions(self):

class BinaryOperation(RandomNumGen):
	def __init__(self):
		RandomNumGen.__init__(self, 2)

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

class UnaryOperation(RandomNumGen):
	def __init__(self):
		RandomNumGen.__init__(self, 1)

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
	
	i
