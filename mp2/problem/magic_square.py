from problem.problem import Problem 
from problem.constraints import *

def problem(N):
	""" Create an NxN magic square """

	# Magic square numbers
	min_number = 1
	max_number = N*N
	numbers = range(min_number,max_number+1)

	# Variables
	variables = []
	for y in range(N): 
		for x in range(N):
			square = '%d,%d' % (x,y) # x,y coords
			variables.append(square)

	# Domain 
	domain = {}
	for var in variables:
		domain[var] = list(numbers)

	# Constraints 
	# Note: Use ExactSum, where sum is magic_sum
	constraints = []
	# Hint: Find out how to solve for magic sum or magic constant
	# magic_sum = ???
	magic_sum = N*((N**2+1)/2)
	# 1) Different number per square
	# INSERT CODE HERE
	varb = []
	for y in range(N):
		for x in range(N):
			varb.append('%d,%d'%(y,x))
	c = AllDifferent(varb,magic_sum);
	c.name = 'AllDiff'
	constraints.append(c)

	# 2) Each column has same total (ExactSum: magic_sum)
	# Note: separate constraint for each column
	# INSERT CODE HERE
	varb = []
	for y in range(N):
		varb = []
		for x in range(N):
			varb.append('%d,%d'% (y,x))
		
		c = ExactSum(varb,magic_sum)
		c.name = ' Exact Sum:Col ' + ('%d' % y)
		constraints.append(c)

	# 3) Each row has same total (ExactSum: magic_sum)
	# Note: separate constraint for each row
	# INSERT CODE HERE

	varb = []
	
	for y in range(N):
		varb = []
		for x in range(N):
			varb.append('%d,%d'% (x,y))
		
		c = ExactSum(varb,magic_sum)
		c.name = 'Exact Sum:Row '  + ('%d' % y)
		constraints.append(c)
	# 4) Forward diagonal has same total (ExactSum: magic_sum)
	# e.g. (0,0), (1,1), ..., (N-1,N-1)
	# INSERT CODE HERE
	varb = []
	for y in range(N):
		varb.append('%d,%d'% (y,y))

	c = ExactSum(varb,magic_sum)
	c.name = ' Exact Sum:Forward Diagonal'
	constraints.append(c)

	# 5) Backward diagonal has same total (ExactSum: magic_sum)
	# e.g. N = 3, (0,2), (1,1), (2,0)
	# INSERT CODE HERE
	varb = []
	for x in range(N):
		varb.append('%d,%d'% (x,(N-x-1)))
	c = ExactSum(varb,magic_sum)
	c.name = 'Exact Sum:Backward Diagonal'
	constraints.append(c)


	# All hard constraints
	for c in constraints:
		c.penalty = float('inf')

	# Create problem
	problem = Problem(variables,domain,constraints)
	problem.name = 'Magic Square'
	problem.N = N
	problem.solution_format = solution_format

	return problem


def solution_format(problem,solution):
	output = []
	N = problem.N
	for y in range(N):
		output.append('\t')
		for x in range(N):
			var = '%d,%d' % (x,y)
			output.append(str(solution[var]).ljust(5))
		output.append('\n')

	return ''.join(output)
