from problem import maxone,knapsack,vertex_cover

from solver.ga import GeneticSolver
from fn.ga import *
from fn.fitness import *
from utils import *

def select_problem(problem_name,config):
    if problem_name == 'maxone':
        problem = maxone.problem(16)
        config.fitness_fn = maxone_fitness
        config.feasibility_minimum = 0
        config.best_possible_score = problem.N
    elif problem_name == 'knapsack':
        problem = knapsack.problem(99)
        config.fitness_fn = knapsack_fitness
        config.feasibility_minimum = 100
        config.best_possible_score = problem.total_value
    elif problem_name == 'vertex_cover':
        problem = vertex_cover.problem(99)
        config.fitness_fn = vertex_cover_fitness
        config.feasibility_minimum = 100
        config.best_possible_score = len(problem.variables)

    return problem

def main():

    # Initialization of parameters to be used for automation

    # POPULATION
    population_size = [20, 50]
    replace_population = [(generational, "generational"), (choose_best, "choose_best")]

    # SELECTION
    max_parent_similarity = [0.9, 0.5] 
    select_parents = [(fitness_proportionate, "fitness_proportionate"), (tournament_selection, "tournament_selection")]

    # CROSSOVER
    prob_crossover = [0.90, 0.60]    
    crossover = [(one_point_crossover, "one_point_crossover"), (two_point_crossover, "two_point_crossover"), (uniform_crossover, "uniform_crossover")]

    # MUTATION
    prob_mutate =  [0.5, 0.3]   
    mutate =  [(change_one_value, "change_one_value"), (change_k_values(2), "change_k_values"), (swap_two_values, "swap_two_values")]

    best_config_list = []

    best_score = 0


    # Configuration starts

    config = Config()

    # problem_name = 'maxone'
    # problem_name = 'knapsack'
    problem_name = 'vertex_cover'

    problem = select_problem(problem_name,config)
    config.best_possible_score += config.feasibility_minimum
    config.initial_solution = 'random'
    config.max_parent_try = 500
    config.max_iterations =  200
    config.max_flat_iterations = 50
    config.random_seed =   123456789
    config.explain = False # Initially True. Set to False to avoid lots of printing in the terminal.

    # Automation starts
    count = 0
    for populationSize in population_size:
        for replacePopulation in replace_population:
            for maxParentSimilarity in max_parent_similarity:
                for selectParents in select_parents:
                    for probCrossover in prob_crossover:
                        for Crossover in crossover:
                            for probMutate in prob_mutate:
                                for Mutate in mutate:


                                    # POPULATION
                                    config.population_size = populationSize     # 20, 50
                                    config.replace_population = replacePopulation[0]
                                    # config.replace_population = choose_best


                                    # SELECTION
                                    config.max_parent_similarity = maxParentSimilarity # 0.9, 0.5
                                    config.select_parents = selectParents[0]
                                    # config.select_parents = tournament_selection
                                    config.tournament_k = int(0.2 * config.population_size)

                                    # CROSSOVER
                                    config.prob_crossover = probCrossover    # 0.90, 0.60
                                    config.crossover = Crossover[0]
                                    # config.crossover = two_point_crossover
                                    # config.crossover = uniform_crossover

                                    # MUTATION
                                    config.prob_mutate = probMutate   # 0.3, 0.5
                                    config.mutate =  Mutate[0]
                                    # config.mutate =  change_k_values(2)
                                    # config.mutate =  swap_two_values

                                    config_list = [
                                                            ("config.population_size",populationSize),
                                                            ("config.replace_population",replacePopulation[1]),
                                                            ("config.max_parent_similarity",maxParentSimilarity),
                                                            ("config.select_parents",selectParents[1]),
                                                            ("config.prob_crossover",probCrossover),
                                                            ("config.crossover",Crossover[1]),
                                                            ("config.prob_mutate",probMutate),
                                                            ("config.mutate",Mutate[1])
                                                        ]
                                    count+=1

                                    # print(count)
                                    # print(config_list)

                                    solver = GeneticSolver(problem,config)
                                    solver.solve()
                                    score = solver.get_best_score()
                                    iterations = solver.get_iterations()
                                    

                                    if score >= best_score:
                                        best_score = score
                                        best_config_list = config_list
                                        print(count)
                                        print(best_config_list)
                                        print("Score:",score)
                                        print("Iterations:",iterations)
                                        print("\n")

                                    # display_solutions(problem,solver)
                                  



if __name__ == '__main__':
    import time
    start = time.time()

    main()

    end = time.time()
    elapsed = end - start
    print('Time elapsed: %ds' % elapsed)

