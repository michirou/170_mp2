def maxone_fitness(state,feasibility_minimum):
	""" Fitness = no. of 1s """
	solution = state.solution
	score = sum(solution.values())
	# always add feasibility_minimum, since there are no constraints
	return feasibility_minimum + score

def knapsack_fitness(state,feasibility_minimum):
	problem = state.problem
	solution = state.solution
	total_value = 0
	total_weight = 0
	excess_weight = 0

	if problem.find_hard_violation(solution) is not None: 
		# has violation: total weight exceeds capacity
		max_score = int(feasibility_minimum * 0.75)

		# INSERT CODE HERE
		# Idea: less excess weight = higher score
		# Hint: use item.weight, problem.capacity
		for sol in solution:
			if solution[sol] == 1:
				total_weight += sol.weight

		excess_weight = abs(problem.capacity-total_weight)

		return abs(max_score-excess_weight)

	else: 
		# no violations
		score = feasibility_minimum # min score for being valid solution

		# INSERT CODE HERE
		# Idea: higher total item value = higher score
		# Hint: use item.value
		for sol in solution:
			if solution[sol] == 1:
				total_value += sol.value

		return score + total_value

def vertex_cover_fitness(state,feasibility_minimum):
	problem = state.problem
	solution = state.solution
	count = 0

	if problem.find_hard_violation(solution) is not None: 
		# has violation: some edges are not covered
		max_score = int(feasibility_minimum * 0.75)
		used_vertices = [v for v in problem.variables if solution[v] == 1]
		unused_vertices = [v for v in problem.variables if solution[v] == 0]

		# INSERT CODE HERE
		# Idea: less uncovered edges = higher score
		# Hint: use problem.edges, used_vertices

		for edge in problem.edges:
			vertex1 = edge[0]
			vertex2 = edge[1]

			if vertex1 and vertex2 in unused_vertices:
				count+=1

		return abs(count - max_score)

	else:	
		# no violations
		score = feasibility_minimum # min score for being valid solution

		# INSERT CODE HERE
		# Idea: less vertices used = better
		# So, higher no. of unused vertices in solution = higher score

		unused_vertices = [v for v in problem.variables if solution[v] == 0]
		for sol in unused_vertices:
			count = count + 1

		return score + count


		


