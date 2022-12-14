"""
    TIMETABLE GENERATOR SIMPLE

"""

__author__ = "Selvaganapathy K"
__email__ = "selvaganz1285@gmail.com"


import numpy as np
from numpy import random
import random


POPULATION_SIZE = 1000


class subject:
    """
    details of each subjects

    """

    def __init__(self, id, name, instructor, hours, year, islab):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.hours = hours
        self.year = year
        self.islab = islab


class Class:
    """
    details of each class in year and day-order

    """

    def __init__(self, day, year, hour):
        self.day = day
        self.year = year
        self.hour = hour
        self.subject = None


class years:
    """
    details of each year of a programme

    """

    def __init__(self, year):
        self.year = year
        self.subjects = []
        self.instructors = []
        self.lab = None


class Instructors:
    """
    details of each year of a programme

    """

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.subjects = {}


def define_each_classes():
    each_classes = {}
    num_dayorders = 6
    num_years = 5
    num_hoursperday = 5
    for i in range(1, num_years + 1):
        each_classes[i] = []
        for j in range(1, num_dayorders + 1):
            each_classes[i].append([])
            for k in range(1, num_hoursperday + 1):
                each_classes[i][j - 1].append(Class(j, i, k))

    return each_classes


def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result


def define_subjects():
    l = {}
    subjects = {
        1: [
            "DP-2:Developmental Psychology – II:NAC:5",
            "GP-2:General Psychology – II:RUK:5",
            "PS-1:Psychological Statistics - I:SRS:5",
            "TAM-1:TAMIL:LANG-1:6",
            "ENG-1:ENGLISH:LANG-2:6",
            "LAB:EP-1:Experimental Psychology- Practical-I :VAO:3",
        ],
        2: [
            "AP-1:Abnormal Psychology-I:KRT:5",
            "RM:Research Methodology:NAC:5",
            "LAP:Legal Aspects of Psychology:SRS:5",
            "TAM-2:TAMIL:LANG-1:5",
            "LANG-2:ENGLISH:LANG-2:5",
            "LAB:EP-3:Experimental Psychology- Practical-III:KAN:3",
            "EDC:IS:Information Security:EDC-1:2",
        ],
        3: [
            "FMCS:Fundamentals of Marketing and Consumer Behavior:RUK:5",
            "FC:Fundamentals of Counselling:ANU:5",
            "FHP:Fundamentals of Health Psychology:KAA:5",
            "PEC:Psychology of Exceptional Children:KAN:5",
            "RP:Rehabilitation Psychology:VAO:5",
            "LAB:EP-5:Experimental Psychology- Practical – V- Case Analysis:KRT:5",
        ],
        4: [
            "OB:Organizational Behavior:ANU:5",
            "CP:Clinical Psychology:RUK:5",
            "PTD:Psychological Testing & Diagnosis:KAA:5",
            "BM:Behavior Modification:VAO:5",
            "LAB:PA:Psychological Assessment- Practical II:SRS:5",
            "EDC:CS:Cyber Security:EDC:5",
        ],
        5: [
            "OB-2:Organizational Behavior - II:NAC:5",
            "MCB:Marketing & Consumer Behavior:KAN:5",
            "CS:Counseling Psychology:KRT:5",
            "HP:Health Psychology:ANU:4",
            "LAB:CA:Case Analysis:KAA:3",
            "EDC:PS:Professional Skills:EDC-2:4",
            "EDC:HRM:Human Resource Management:EDC-3:4",
        ],
    }
    for j in subjects:
        l[j] = []
        for k in subjects[j]:
            z = k.split(":")
            if len(z) == 4:
                l[j].append(subject(z[0], z[1], z[2], z[3], j, False))
            else:
                l[j].append(subject(z[1], z[2], z[3], z[-1], j, z[0] == "LAB"))
    return l


def define_staffs(each_subjects):
    check = {}
    for i, j in each_subjects.items():
        for k in j:
            if k.instructor not in check:
                x = Instructors(k.instructor, k.instructor)
                x.subjects[k.year] = k

                check[k.instructor] = x
            else:
                check[k.instructor].subjects[k.year] = k

    return check


def details_of_each_year(subject_details):
    year = []
    for j in subject_details:
        x = years(j)
        for k in subject_details[j]:
            if k.year == j:
                x.subjects.append(k.name)
                x.instructors.append(k.instructor)
                if k.islab:
                    x.lab = k

        year.append(x)
    return year


def schedule_labs(each_year, each_class):
    lab_hours = []
    for i in each_year:
        num_hours = int(i.lab.hours)
        while num_hours >= 1:
            f = random.randint(0, 29)

            conflicts = [
                each_class[z][f // 5][f % 5].subject
                for z in range(1, 6)
                if each_class[z][f // 5][f % 5].subject is not None
            ]
            sec_conflict = [each_class[i.year][f // 5][z].subject for z in range(5)]

            if conflicts == [] and i.lab not in sec_conflict:
                if num_hours >= 2:
                    fetch = (f // 5, (f % 5) + 1)
                    s_fetch = (f // 5, f % 5)
                    if (
                        f % 5 != 4
                        and fetch not in lab_hours
                        and s_fetch not in lab_hours
                    ):
                        each_class[i.year][f // 5][(f % 5) + 1].subject = i.lab
                        each_class[i.year][f // 5][f % 5].subject = i.lab
                        lab_hours.extend([(f // 5, (f % 5) + 1)])
                        lab_hours.extend([(f // 5, f % 5)])
                        num_hours -= 2
                if num_hours == 1:
                    fetch = (f // 5, f % 5)
                    if fetch not in lab_hours:
                        each_class[i.year][f // 5][f % 5].subject = i.lab
                        lab_hours.extend([(f // 5, f % 5)])
                        num_hours -= 1


def display_classes(each_class):
    it = {}
    for i, t in each_class.items():
        print("YEAR:", i)
        print(" ".join(["{:5}".format(q) for q in range(1, 6)]))
        z = 1
        it[i] = {}
        for k in t:
            print(
                z,
                " ".join(
                    [
                        "{:5}".format(p.subject.id)
                        if p.subject != None
                        else "{:5}".format("None")
                        for p in k
                    ]
                ),
            )
            z += 1
        print()


def shuffle_classes(each_subject, each_class, each_staff):
    d = {}
    for i, t in each_subject.items():
        d[i] = {}
        for k in t:
            d[i][k] = int(k.hours)

    for i in range(30):
        for x in range(1, 6):

            subj = each_class[x][i // 5][i % 5]
            if subj.subject is not None and not subj.subject.islab:
                subj.subject = None

            else:
                pass

    misbehaviour = 0
    staff_db = {1: [], 2: []}
    for i in range(30):
        staffs = [
            each_class[z][i // 5][i % 5].subject.instructor
            for z in range(1, 6)
            if each_class[z][i // 5][i % 5].subject is not None
        ]
        z = 0
        # print(i//5,i%5)
        for x in range(1, 6):
            subj = each_class[x][i // 5][i % 5]
            if subj.subject is None:
                required_staffs = [
                    t
                    for q, t in each_staff.items()
                    if x in t.subjects
                    and t.name not in staffs
                    and not (t.name in staff_db[1] and t.name not in staff_db[2])
                ]
                # print(x)
                # print('rs',[e.name for e in required_staffs])
                picked_staffs = [
                    s
                    for s in required_staffs
                    if not s.subjects[x].islab and d[x][s.subjects[x]] != 0
                ]
                # print('ps',[e.name for e in picked_staffs])
                if picked_staffs != []:
                    picked_staff = random.choice(picked_staffs)
                    picked_subject = picked_staff.subjects[x]
                    subj.subject = picked_subject
                    staffs.append(picked_staff.name)
                    d[x][picked_subject] -= 1
                else:
                    misbehaviour += 1
            staff_db[2] = staff_db[1]
            staff_db[1] = staffs
    # print("Total Missed:",a)

    # for i,j in sorted(ind.items()):
    #     print(i,*j)

    return misbehaviour


def debug_result(each_class):
    chk = []
    it = {}
    for i, j in each_class.items():
        it[i] = {"None": 0}
        for k in j:
            for p in k:
                if p.subject is not None:
                    if p.subject.name + "-" + p.subject.hours not in it[i]:
                        it[i][p.subject.name + "-" + p.subject.hours] = 1
                    else:
                        it[i][p.subject.name + "-" + p.subject.hours] += 1
                else:
                    it[i]["None"] += 1

    for i, j in it.items():
        print(i)
        for k, l in j.items():
            print(k, l)
            if k != "None":
                chk.append(k[-1] == str(l))
        print("\n")

    if not all(chk):
        print("Produced timetable is incorrect ")
    else:
        print("Produced timetable is correct")


class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.sched = self.get_schedule()
        self.fitness = self.cal_fitness()

    @classmethod
    def create_gnome(self):
        each_class = define_each_classes()
        each_subject = define_subjects()
        each_year = details_of_each_year(each_subject)
        schedule_labs(each_year, each_class)
        each_staff = define_staffs(each_subject)
        while True:
            x = shuffle_classes(each_subject, each_class, each_staff)
            if x == 0:
                break

        # display_classes(each_class)
        # debug_result(each_class)
        return each_class

    def cal_fitness(self):
        fit = 0
        sched = self.sched

        for i, j in sched.items():
            for x, y in j.items():
                consecutives = group_consecutives(sorted(y))
                for every in consecutives:
                    if len(every) >= 4:
                        fit += 1

        for i,j in self.chromosome.items():
            for k in j:
                l=set([q.subject.name for q in k])
                if len(l)<=2:
                    fit+=1


        return fit

    def get_schedule(self):
        sched = {}
        for i, j in self.chromosome.items():
            ind_x = 1
            for x in j:
                ind_y = 1
                for y in x:
                    if y.subject.instructor not in sched:
                        sched[y.subject.instructor] = {ind_x: [ind_y]}
                    else:
                        if ind_x in sched[y.subject.instructor]:
                            sched[y.subject.instructor][ind_x].extend([ind_y])
                        else:
                            sched[y.subject.instructor][ind_x] = [ind_y]
                    ind_y += 1
                ind_x += 1

        return sched


def main():

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population

    while not found:
        every_gnome = Individual.create_gnome()
        gnome = Individual(every_gnome)
        
        if gnome.fitness <= 0:
            found = True
        print(f"GENERATION:{generation},fitness:{gnome.fitness}")

        generation += 1  # sort the population in increasing order of fitness score

        # break
        # break
        # Otherwise generate new offsprings for new generation

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation

    it = {}
    for i, t in gnome.chromosome.items():
        it[i] = []
        x = 0
        for k in t:
            it[i].append([])
            for p in k:
                if not p.subject is None:
                    it[i][x].append(p.subject.name)
            x += 1
    print(it)
    display_classes(gnome.chromosome)
    return it


if __name__ == "__main__":

    result = main()

"""
INCORRECTLY WORKING FUNCTIONS:
1. Individual.cal_fitiness()
2. shuffle_classes()
"""
