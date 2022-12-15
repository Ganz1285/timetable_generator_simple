import sqlite3
import numpy as np
from numpy import random
import random

con=sqlite3.connect("try.db")

POPULATION_SIZE = 100


class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        # self.sched=self.get_schedule()
        self.fitness = self.cal_fitness()
    @classmethod
    def subjects(self):
        subjects = [[], [], [], [], []]
        for i in range(5):
            for row in cur.execute(f"SELECT subject_id,staff_id,hours FROM subjects WHERE year=={i+1};"):
                subjects[i].append(str(row[0]+':'+row[1]+":"+str(row[2])))

        return(subjects)



    @classmethod
    def create_gnome(self):
        sub=self.subjects()
        d={}
        j=1
    
    
        for i in sub:
            l=np.array([j[:-2] for j in i for _ in range(int(j[-1]))])
            np.random.shuffle(l)
            d[j]=l.reshape(6,5)
            j+=1
    
    
    
        return d

    def cal_fitness(self):
        return random.choice([i for i in range(10)])


def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))
        
    while not found:

      # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)
        
        if population[0].fitness <= 0:
            found = True
            break

        

if __name__ =="__main__":
    cur=con.cursor()
    main()
    con.close()
    
    
    

        