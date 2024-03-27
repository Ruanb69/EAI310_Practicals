import csv
import random as R


class specimen:
    fitness = 0

    def __init__(self, genetics):
        self.genetics = genetics
        self.specimen_sequence = [0] * 81
        for i in range(81):
            self.specimen_sequence[i] = genetics[i][1]
            self.fitness += genetics[i][0]
        self.fitness = self.fitness / len(self.genetics)

    def get_output(self):
        return self.specimen_sequence

    def get_fitness(self):
        return self.fitness


def read_csv_file(filename, population_size):
    specimen_list = []
    genetics_for_node = [[] for _ in range(81)]
    game1_event = ""
    game1_result = 0
    game2_event = ""
    game2_result = 0
    specimen_fitness = 0
    node_count = 0
    opponent_move = ""
    specimen_move = ""
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        row_counter = 0
        for row in reader:
            opponent_move = row[1]
            game1_event = row[0][2:]  # substring of first 2 chars
            game2_event = row[0][:2]  # substring of last 2 chars
            # Analyse the previous 2 games and quantify scores
            if game1_event in [ "RR" , "PP" , "SS"]:
                game1_result = 25
            if game2_event in [ "RR" , "PP" , "SS"]:
                game2_result = 25
            if game1_event in [ "PR" , "RS" , "SP"]:
                game1_result = 50
            if game2_event  in [ "PR" , "RS" , "SP"]:
                game2_result = 50
            if game1_event  in [ "RP" , "SR" , "PS"]:
                game1_result = 0
            if game2_event in [ "RP" , "SR" , "PS"]:
                game2_result = 0
            specimen_fitness = game1_result + game2_result
            # Choose move to play
            if opponent_move == "P":
                specimen_move = "S"
            if opponent_move == "S":
                specimen_move = "R"
            if opponent_move == "R":
                specimen_move = "P"
            # Assign gene in the genetics array
            genetics_for_node[row_counter] = [specimen_fitness, specimen_move]
            row_counter += 1
            if row_counter == 81:
                # Node sequence has been filled
                # Append Specimen to the population
                specimen_list.append(specimen(genetics_for_node))
                # Clear the array for next node and reset placeholder
                genetics_for_node = [[] for _ in range(81)]
                row_counter = 0
                node_count += 1

            if population_size == node_count:
                # The desired population has been reached
                return specimen_list


def merge_sort_by_fitness(population):
    if len(population) > 1:
        mid = len(population) // 2
        left_half = population[:mid]
        right_half = population[mid:]

        merge_sort_by_fitness(left_half)
        merge_sort_by_fitness(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].get_fitness() > right_half[j].fitness:
                population[k] = left_half[i]
                i += 1
            else:
                population[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            population[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            population[k] = right_half[j]
            j += 1
            k += 1


def selection_and_crossover(specimens, type, population_size: int, mutation_rate: float):
    # Crossover methods:
    #       Random selection: "R"
    #       Percentage selection: "P"
    #       Half-and-Half: "H"

    # Selection method: Survival of the fittest!
    merge_sort_by_fitness(specimens)
    new_generation = []
    if type == "R":  # Random selection
        # Initialise arrays for the offspring
        i = 0
        new_Dna_1 = []
        new_Dna_2 = []
        random_index = 0
        while i in range(population_size):
            temp = []
            temp2 = []
            random_index = R.randint(0, 80)  # This random number decides the split point in indexes
            for j in range(random_index):
                # Create temp array appending the first part of the FIRST specimen's DNA up until the split point
                temp.append(specimens[i].genetics[j])
                # Create temp array appending the first part of the SECOND specimen's DNA up until the split point
                temp2.append(specimens[i + 1].genetics[j])

            # Now attach the other parts of the two specimens
            for k in range(81 - random_index):
                # Append the other part of the SECOND specimen's DNA
                temp.append(specimens[i + 1].genetics[k])
                # Append the other part of the FIRST specimen's DNA
                temp2.append(specimens[i].genetics[k])
            # Create new specimens with new DNA.
            new_generation_specimen1 = specimen(temp)
            new_generation_specimen2 = specimen(temp2)
            # Mutate the offspring
            mutation(new_generation_specimen1, mutation_rate)
            mutation(new_generation_specimen2, mutation_rate)
            # Add the new kids to the population
            new_generation.append(new_generation_specimen1)
            new_generation.append(new_generation_specimen2)
            i += 2  # Skip over two places to work with next pair
        return new_generation
        # mergeDna = []
        # while i in range(len(newDna)):
        #     mergeDna.append(newDna[i] + newDna_2[i + 1])
        #     mergeDna.append(newDna[i + 1] + newDna_2[i])
        #     i += 2
        # return mergeDna

    elif type == "P":  # Percentage selection
        i = 0
        while i in range(population_size):
            temp = []
            temp2 = []
            percentage_index = int(specimens[i].get_fitness() / 100 * 81)
            for j in range(percentage_index):
                # Create temp array appending the first part of the FIRST specimen's DNA up until the split point
                temp.append(specimens[i].genetics[j])
                # Create temp array appending the first part of the SECOND specimen's DNA up until the split point
                temp2.append(specimens[i + 1].genetics[j])

            # Now attach the other parts of the two specimens
            for k in range(81 - percentage_index):
                # Append the other part of the SECOND specimen's DNA
                temp.append(specimens[i + 1].genetics[k])
                # Append the other part of the FIRST specimen's DNA
                temp2.append(specimens[i].genetics[k])
            # Create new specimens with new DNA
            new_generation_specimen1 = specimen(temp)
            new_generation_specimen2 = specimen(temp2)
            # Mutate the offspring
            mutation(new_generation_specimen1, mutation_rate)
            mutation(new_generation_specimen2, mutation_rate)
            # Add the new kids to the population
            new_generation.append(new_generation_specimen1)
            new_generation.append(new_generation_specimen2)
            i += 2  # Skip over two places to work with next pair
        i = 0

        return new_generation
    elif type == "H":  # Half-and-Half
        i = 0
        half_index = 40
        while i in range(population_size):
            temp = []
            temp2 = []
            for j in range(half_index):
                # Create temp array appending the first part of the FIRST specimen's DNA up until the split point
                temp.append(specimens[i].genetics[j])
                # Create temp array appending the first part of the SECOND specimen's DNA up until the split point
                temp2.append(specimens[i + 1].genetics[j])

            # Now attach the other parts of the two specimens
            for k in range(81 - half_index):
                # Append the other part of the SECOND specimen's DNA
                temp.append(specimens[i + 1].genetics[k])
                # Append the other part of the FIRST specimen's DNA
                temp2.append(specimens[i].genetics[k])
            # Create new specimens with new DNA
            new_generation_specimen1 = specimen(temp)
            new_generation_specimen2 = specimen(temp2)
            # Mutate the offspring
            mutation(new_generation_specimen1, mutation_rate)
            mutation(new_generation_specimen2, mutation_rate)
            # Add the new kids to the population
            new_generation.append(new_generation_specimen1)
            new_generation.append(new_generation_specimen2)
            i += 2  # Skip over two places to work with next pair
        i = 0

        return new_generation

    else:
        print("invalid selection type")


def mutation(offspring, mutation_rate):
    mutation_count = 0
    for i in range(len(offspring.genetics)):

        if mutation_rate > R.randrange(0,1000):
            mutation_count += 1
            if offspring.genetics[i][1] == "R":
                offspring.genetics[i][1] = "S"
            elif offspring.genetics[i][1] == "P":
                offspring.genetics[i][1] = "R"
            elif offspring.genetics[i][1] == "S":
                offspring.genetics[i][1] = "P"
    print("This specimen has mutated" + str(mutation_count) + " times")
    return


def main():
    csv_file = "data1.csv"
    population = read_csv_file(csv_file, 4)
    # print(population)
    # genetics_array = [[] for _ in range(81)]
    # for i in range(81):
    #     genetics_array[i] = [75, "R"]
    # specimen_1 = specimen(genetics_array)
    # print(specimen_1.get_output())
    # print(int(specimen_1.get_fitness()))
    #
    # genetics_array1 = [[] for _ in range(81)]
    # for i in range(81):
    #     genetics_array1[i] = [100, "S"]
    # specimen2 = specimen(genetics_array1)
    # print(specimen2.get_output())
    # print(int(specimen2.get_fitness()))
    #
    # genetics_array2 = [[] for _ in range(81)]
    # for i in range(81):
    #     genetics_array2[i] = [50, "P"]
    # specimen3 = specimen(genetics_array2)
    # print(specimen3.get_output())
    # print(int(specimen3.get_fitness()))
    #
    # genetics_array3 = [[] for _ in range(81)]
    # for i in range(81):
    #     genetics_array3[i] = [0, "R"]
    # specimen4 = specimen(genetics_array3)
    # print(specimen4.get_output())
    # print(int(specimen4.get_fitness()))
    #
    # population = [specimen_1, specimen2, specimen3, specimen4]

    first_generation = selection_and_crossover(population, "R", 4, 0.1)

    for i in range(len(population)):
        print(first_generation[i].get_output())
        print(int(first_generation[i].get_fitness()))

    second_generation = selection_and_crossover(first_generation, "P", 4, 0.1)

    for i in range(len(population)):
        print(second_generation[i].get_output())
        print(int(second_generation[i].get_fitness()))

    third_generation = selection_and_crossover(second_generation, "H", 4, 0.1)

    for i in range(len(population)):
        print(third_generation[i].get_output())
        print(int(third_generation[i].get_fitness()))

    fourth_generation = selection_and_crossover(second_generation, "H", 4, 0.1)

    for i in range(len(population)):
        print(fourth_generation[i].get_output())
        print(int(fourth_generation[i].get_fitness()))

    # filename = 'data2.csv'
    # read_csv_file(filename, population_size=2)


main()
