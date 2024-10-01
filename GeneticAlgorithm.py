import random
import math
from PIL import Image

POPULATION_SIZE = 100
MUTATION_RATE = 0.05
N_ITER_MAX = 200

def getPixel(x): 
    pixel = (x%16, math.floor(x/16))
    return pixel

def getPixelColor(pixel, img):
    return img[pixel[0], pixel[1]]

def generate_initial_population(size, n):
    population = []
    for i in range(size):
        rand = sorted(random.sample(range(0, 256), n))
        population.append(rand)
    return population


def getError(individual, letters):
    d = dict((key, []) for key in list(letters.keys()))
    for x in individual:
        pixel = getPixel(x)
        for key in letters.keys():
            d[key].append(getPixelColor(pixel, letters[key]))
    
    listValues = list(d.values())
    error = 0
    setValues = set(tuple(i) for i in listValues)
    error = len(listValues) - len(setValues)
    return error

def fitness(individual, letters, weightMap):
    error = getError(individual, letters)
    fitness = -0.00000001
    
    for x in individual:
        pixel = getPixel(x)
        fitness += getPixelColor(pixel, weightMap)/len(individual)
    return fitness - error

def crossover(parent1, parent2, n):
    crossover_point = random.randint(1, n-1)
    child1 = parent1[:crossover_point]
    child2 = parent2[:crossover_point]

    for i in range(crossover_point, n):
        
        if not parent2[i] in child1:
            child1.append(parent2[i])
        else:
            cont = 0
            while (parent2[i]+cont)%256 in child1:
                cont += 1
            child1.append((parent2[i]+cont)%256)

        if not parent1[i] in child2:
            child2.append(parent1[i])
        else:
            cont = 0
            while (parent1[i]+cont)%256 in child2:
                cont += 1
            child2.append((parent1[i]+cont)%256)

    child1.sort()
    child2.sort()
    return child1, child2

def mutate(individual):
    mutated_individual = []
    possibleMutations = [i for i in range(256)]
    for pixel in individual:
        possibleMutations.remove(pixel)

    for pixel in individual:
        if random.random() < MUTATION_RATE:
            randomNumber = random.choice(possibleMutations)
            possibleMutations.remove(randomNumber)
            mutated_individual.append(randomNumber)
        else:
            mutated_individual.append(pixel)
    mutated_individual.sort()        
    return mutated_individual

def select_parents(population, letters, weightMap):
    fitnesses = [fitness(individual, letters, weightMap) for individual in population]
    sum_fitnesses = sum(fitnesses)
    probabilities = [sum_fitnesses / fitness for fitness in fitnesses]
    parent1, parent2 = random.choices(population, weights=probabilities, k=2)
    return parent1, parent2

def select_parents2(population, letters, weightMap):
    fitnesses = [fitness(individual, letters, weightMap) for individual in population]
    fitnessesDict = dict((i, fitnesses[i]) for i in range(len(population)))
    sort = sorted(fitnessesDict, key=lambda x: fitnessesDict[x])[math.floor(len(population)/2):]
    #sort = [x[0] for x in sort]
    fileredPopulation = [population[x] for x in sort]
    parent1, parent2 = random.choices(fileredPopulation, k=2)
    return parent1, parent2

def evolve(population, letters, n, weightMap):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        parent1, parent2 = select_parents2(population, letters, weightMap)
        child1, child2 = crossover(parent1, parent2, n)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population

def geneticAlgorithm(letters, N, weightMap):

    population = generate_initial_population(POPULATION_SIZE, N)
    generation = 0

    best_sol = []
    best_fit = -10000

    while generation < N_ITER_MAX:
        fitnesses = [fitness(individual, letters, weightMap) for individual in population]
        max_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(max_fitness)]
        if (max_fitness>best_fit):
            best_sol = best_individual
            best_fit = max_fitness
        print(f"Generation {generation}, best individual: {best_individual}, fitness: {max_fitness}")
        if max_fitness >= 0:
            print("SOLUTION FOUND")
            break
        
        population = evolve(population, letters, N, weightMap)
        generation += 1

    return best_sol, best_fit