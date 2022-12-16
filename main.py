import sqlite3
import numpy as np
from numpy import random
import random

con=sqlite3.connect("try.db")

POPULATION_SIZE = 100



def subjects():
        subjects = [[], [], [], [], []]
        for i in range(5):
            for row in cur.execute(f"SELECT subject_id,staff_id,hours FROM subjects WHERE year=={i+1};"):
                subjects[i].append(str(row[0]+':'+row[1]+":"+str(row[2])))
        return(subjects)



class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        # self.sched=self.get_schedule()
        self.fitness = self.cal_fitness()
        self.subjects=subjects()
    @classmethod
    


    @classmethod
    def create_gnome(self):
        sub=SUBJECTS
        d={}
        j=1
    
    
        for i in sub:
            l=np.array([j[:-2] for j in i for _ in range(int(j[-1]))])
            np.random.shuffle(l)
            k=l.reshape(6,5)

            d[j]=np.sort(k)
            j+=1
    
    
    
        return d

    def cal_fitness(self):
        fit=0


        #lab classes 
        for i in range(1,6):
            lst=[]
            for j in self.chromosome[i]:
                k=[l.split(':')[0]for l in j]
                a=sum([+1 for z in k if z=='LAB'])
                if a!=0:lst.append(a)
            if i !=4 and sorted(lst)!=[1,2]:
                fit+=1
            elif i == 4 and sorted(lst)!=[1,2,2]:
                fit+=1

        

        return fit

    def mate(self,par2):
        l={}
        for i in range(1,6):
            lst=[]
            for j,p in zip(self.chromosome[i],par2.chromosome[i]):
                prob=random.random()
                if prob<0.50:
                    lst.append(j)
                elif prob<1.0:
                    lst.append(p)
                else:
                    lst.append(self.mutated_genes(i))
            l[i]=np.array(lst)
        
        return Individual(l)

    # def mutated_genes(self,year):
        
    #     return random.choice(Individual.create_gnome()[year])


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
            # break
            # break
            # Otherwise generate new offsprings for new generation
        new_generation = []

      # Perform Elitism, that mean 10% of fittest population
      # goes to the next generation
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
      # will mate to produce offspring
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation

        print(f"Generation:{generation}")
        print(population[0].chromosome)
        print(f"Fitness:{population[0].fitness}")

        generation += 1
    print(f"Generation:{generation}")
    print(population[0].chromosome)
    print(f"Fitness:{population[0].fitness}")

if __name__ =="__main__":
    cur=con.cursor()
    SUBJECTS = subjects()

    main()
    con.close()
    
    
    

        