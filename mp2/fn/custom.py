import random 

### CUSTOM NEIGHBOR GENERATORS ###

def maxone_neighbor_generator(state):
    problem = state.problem
    solution = state.solution

    while True:
        neighbor = state.copy()

        # Flip a random 0 to 1
        value = None
        while value != 0:
            # randomly select var with value 0 assigned in solution
            var = random.choice(problem.variables)
            value = solution[var]

        new_value = 1
        neighbor.solution[var] = new_value
        neighbor.changes = [(var,new_value)]
        yield neighbor


def knapsack_neighbor_generator(state):
    problem = state.problem
    solution = state.solution
    constraint = problem.constraints[0]

    passed = constraint.test(solution)
    while True:
        neighbor = state.copy()

        # INSERT CODE HERE
        #       If knapsack is not yet full, neighbor = randomly change up to 2 values (includes adding item, removing item, swapping)
        # Idea: If knapsack is already full, neighbor = remove a random item from current solution (try to remove excess)
        # Hint: use constraint.test(solution)
        # Hint: check the pattern of maxone_neigbor_generator
        # Dont forget to update neighbor.changes

        if(passed):
            var1 = random.choice(problem.variables)         
            var2 = random.choice(problem.variables)     
            value1 = random.choice(problem.domain[var1])
            value2 = random.choice(problem.domain[var2])
            
            solution_var1 = state.solution[var1]
            solution_var2 = state.solution[var2]


            neighbor = state.copy()   
            if value1 == solution_var1 and value2 != solution_var2:
                neighbor.solution[var2] = value2
                neighbor.changes = [(var2,value2)]

            else:
                neighbor.solution[var1] = value1
                neighbor.solution[var2] = value2
                neighbor.changes = [(var1,value1), (var2, value2)]

            yield neighbor

        else:
            value = None
            while value != 1:
                var = random.choice(problem.variables)
                value = solution[var]

            new_value = 0
            neighbor.solution[var] = new_value
            neighbor.changes = [(var,new_value)]

        yield neighbor
        

def vertex_cover_neighbor_generator(state):
    problem = state.problem
    solution = state.solution
    constraint = problem.constraints[0]
    passed = constraint.test(solution)
    
    while True:
        neighbor = state.copy()

        # INSERT CODE HERE
        # Idea: If all edges not yet covered, neighbor = add a random vertex to current solution (try to add more edges covered)
        #       If all edges already covered, neighbor = remove a random vertex from current solution (try to minimize no. of vertex used)
        # Hint: use constraint.test(solution)
        # Hint: check the pattern of maxone_neigbor_generator
        # Dont forget to update neighbor.changes

        if(passed):
            value = None
            while value != 1:
                var = random.choice(problem.variables)
                value = solution[var]

            new_value = 0
            neighbor.solution[var] = new_value
            neighbor.changes = [(var,new_value)]


        else:
            value = None
            while value != 0:
                var = random.choice(problem.variables)
                value = solution[var]

            new_value = 1
            neighbor.solution[var] = new_value
            neighbor.changes = [(var,new_value)]


        yield neighbor
