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
                        output = 1
                else:
                        output = 0

                return output

class QuestionGenerator(BinaryOperation, UnaryOperation, ValidAnswer):
	operation_dict = {'addition' : addition, 'subtraction' : subtraction, 'multiplication' : multiplication, 'exponentiation' : exponentiation, 
		'division' : division, 'square root' : square_root, 'perfect square' : perfect_square}
	operation_symbol_dict = {'addition' : '+', 'subtraction' : '-', 'multiplication' : 'x', 'division' : '/', 'exponentiation' : '^', 
		 'square root' : 'Square root of ', 'perfect square' : 'Perfect square of '}

	def __init__(self, operation_type = ['addition'], lower_bound = 2, upper_bound= 100, num_seconds):
		self.operation_type = operation_type
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
		self.num_seconds = num_seconds
	
	def generate_question(self):
		total_question_count = 0
		correct_count = 0
		if len(self.operation_type) < 1:
			print("Please input an operation you'd like to be tested on.")
		
		if self.operation_type[0] == 'all':
			for operation in operation_dict.keys():
				symbol = operation_symbol_dict[operation]
				if operation in ['addition', 'subtraction', 'multiplication', 'division', 'exponentiation']:
					# print problem for user to compute
					oper_obj = BinaryOperation()
					operand1, operand2 = oper_obj.operands
					answer = oper_obj.operation_dict[operation]()

					try:
						user_input = int(input("{num_1} {symbol} {num_2}".format(num_1 = operand1, symbol = symbol, num_2 = operand2))) 
					
					except ValueError:
    						print("Enter a number only.")
						        continue

					# validate user answer
					checker = ValidAnswer(user_input, answer)
					correct_count += checker.check_answer
			
				elif operation in ['square root', 'perfect square']:
					# print problem for user to compute
                                            oper_obj = UnaryOperation()
                                            operand1 = oper_obj.operands
                                            answer = oper_obj.operation_dict[operation]()
                                            
					try:
                                                    user_input = int(input("{symbol} {num_1}".format(symbol = symbol, num_1 = operand1)))
						total_question_count += 1

                                            except ValueError:
                                                    print("Enter a number only.")
                                                    continue

                                            # validate user answer
                                            checker = ValidAnswer(user_input, answer)
                                            correct_count += checker.check_answer
		else:
			for operation in self.operation_type:
				symbol = operation_symbol_dict[operation]
                                    if operation in ['addition', 'subtraction', 'multiplication', 'division', 'exponentiation']:
                                            # print problem for user to compute
                                            oper_obj = BinaryOperation()
                                            operand1, operand2 = oper_obj.operands
                                            answer = oper_obj.operation_dict[operation]()

                                            try:
                                                    user_input = int(input("{num_1} {symbol} {num_2}".format(num_1 = operand1, symbol = symbol, num_2 = operand2)))
						total_question_count += 1

                                            except ValueError:
                                                    print("Enter a number only.")
                                                    continue

                                            # validate user answer
                                            checker = ValidAnswer(user_input, answer)
                                            correct_count += checker.check_answer

                                    elif operation in ['square root', 'perfect square']:
                                            # print problem for user to compute
                                            oper_obj = UnaryOperation()
                                            operand1 = oper_obj.operands
                                            answer = oper_obj.operation_dict[operation]()

                                            try:
                                                    user_input = int(input("{symbol} {num_1}".format(symbol = symbol, num_1 = operand1)))

                                            except ValueError:
                                                    print("Enter a number only.")
                                                    continue

                                            # validate user answer
                                            checker = ValidAnswer(user_input, answer)
                                            correct_count += checker.check_answer

		print("Time's up. You got {x} questions correct out of {y} total questions".format(x = correct_count, y = total_question_count)) 
					
					
					









