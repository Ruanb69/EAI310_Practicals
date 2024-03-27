import random as R
class specimen():
    fitness = 0

    def __init__(self, genetics):
        self.genetics = genetics
        self.output_line = [genetics[1] for _ in range(81)]

    def get_output(self):
        return self.output_line
    def get_fitness(self):
        return self.fitness
def read_csv_file(filename, population_size):
    population = [Node for _ in range(population_size)]
    game1_event = ""
    game1_result = 0
    game2_event = ""
    game2_result = 0
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
    row_counter = 0
    for row in reader:
        game1_event = row[0][:2]
        game2_event = row[0][2:]
        print(game1_event)
        print(game2_event)
        # row_counter += 1
        # if rowCounter == 80:
        #     population.append(Node())


def selection_and_crossover(specimens , type, pop_size: int):
    if type == "R":
        i = 0
        newDna = []
        newDna_2 = []
        random_index = 0
        while i in range(pop_size):
            temp = []
            temp2 = []
            for j in range(40):
                random_index = R.randint(0, 81)
                temp.append(specimens[i].get_output()[random_index])
                random_index = R.randint(0, 81)
                temp2.append(specimens[i].get_output()[random_index])
            newDna.append(temp)
            newDna_2.append(temp2)
            i += 1
            for j in range(41):
                random_index = R.randint(0, 81)
                temp.append(specimens[i].get_output()[random_index])
                random_index = R.randint(0, 81)
                temp2.append(specimens[i].get_output()[random_index])

            newDna.append(temp)
            newDna_2.append(temp2)
            i += 1
        i = 0
        mergeDna = []
        while i in range(len(newDna)):
            mergeDna.append(newDna[i] + newDna_2[i + 1])
            mergeDna.append(newDna[i + 1] + newDna_2[i])
            i += 2
        return mergeDna

    elif type == "S":
        i = 0
        newDna = []
        newDna_2 = []

        while i in range(pop_size):
            percentage_index = int(specimens[i].get_fitness() * 81)
            temp = (specimens[i].get_output()[::percentage_index])
            temp2 = (specimens[i].get_output()[percentage_index::])
            newDna.append(temp)
            newDna.append(temp2)
            i += 1
            percentage_index = int(specimens[i].get_fitness() * 81)
            temp = (specimens[i].get_output()[::percentage_index])
            temp2 = (specimens[i].get_output()[percentage_index::])
            newDna_2.append(temp)
            newDna_2.append(temp2)

            i += 1
        i = 0
        mergeDna = []
        while i in range(len(newDna)):
            mergeDna.append(newDna[i] + newDna_2[i + 1])
            mergeDna.append(newDna[i + 1] + newDna_2[i])
            i += 2
        return mergeDna
    elif type == "H":
        i = 0
        newDna = []
        newDna_2 = []

        while i in range(pop_size):
            half_index = 40
            temp = (specimens[i].get_output()[::half_index])
            temp2 = (specimens[i].get_output()[half_index::])
            newDna.append(temp)
            newDna.append(temp2)
            i += 1
            half_index = 40
            temp = (specimens[i].get_output()[::half_index])
            temp2 = (specimens[i].get_output()[half_index::])
            newDna_2.append(temp)
            newDna_2.append(temp2)

            i += 1
        i = 0
        mergeDna = []
        while i in range(len(newDna)):
            mergeDna.append(newDna[i] + newDna_2[i + 1])
            mergeDna.append(newDna[i + 1] + newDna_2[i])
            i += 2
        return mergeDna

    else:
        print("invalid selection type")


def main():
    genetics_array = []
    genetics_array[0][0] = "R"
    print(genetics_array)
    genetics_array[0][1] = "P"
    print(genetics_array)
    my_specimen = specimen(genetics_array)
    print(my_specimen.output_line)
    filename = 'data2.csv'
    read_csv_file(filename, population_size=2)

