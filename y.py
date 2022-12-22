import numpy as np
from numpy import random


class subject:
    def __init__(self,id,name,instructor,hours,year,islab):
        self.id=id
        self.name=name
        self.instructor=instructor
        self.hours=hours
        self.year=year
        self.islab=islab




class Class:
    def __init__(self,day,year,hour):
        self.day=day
        self.year=year
        self.hour=hour
        self.subject=None




class years:
    def __init__(self,year):
        self.year=year
        self.subjects=[]
        self.instructors=[]
        self.lab=None


class labs:
    def __init__(self):
        self.year=year



each_classes=[]
num_dayorders=6
num_years=5
num_hoursperday=5
for i in range(1,num_dayorders+1):
    for j in range(1,num_years+1):
        for k in range(1,num_hoursperday+1):
                each_classes.append(Class(i,j,k))


l={}
subjects={1:['DP-2:Developmental Psychology – II:NAC:5', 'GP-2:General Psychology – II:RUK:5', 'PS-1:Psychological Statistics - I:SRS:5', 'TAM-1:TAMIL:LANG-1:6', 'ENG-1:ENGLISH:LANG-2:6', 'LAB:EP-1:Experimental Psychology- Practical-I :VAO:3'],2: ['AP-1:Abnormal Psychology-I:KRT:5', 'RM:Research Methodology:NAC:5', 'LAP:Legal Aspects of Psychology:SRS:5', 'TAM-2:TAMIL:LANG-1:5', 'LANG-2:ENGLISH:LANG-2:5', 'LAB:EP-3:Experimental Psychology- Practical-III:KAN:3', 'EDC:IS:Information Security:EDC:2'],3: ['FMCS:Fundamentals of Marketing and Consumer Behavior:RUK:5', 'FC:Fundamentals of Counselling:ANU:5', 'FHP:Fundamentals of Health Psychology:KAA:5', 'PEC:Psychology of Exceptional Children:KAN:5', 'RP:Rehabilitation Psychology:VAO:5', 'LAB:EP-5:Experimental Psychology- Practical – V- Case Analysis:KRT:5'],4: ['OB:Organizational Behavior:ANU:5', 'CP:Clinical Psychology:RUK:5', 'PTD:Psychological Testing & Diagnosis:KAA:5', 'BM:Behavior Modification:VAO:5', 'LAB:PA:Psychological Assessment- Practical II:SRS:5', 'EDC:CS:Cyber Security:EDC:5'],5: ['OB-2:Organizational Behavior - II:NAC:5', 'MCB:Marketing & Consumer Behavior:KAN:5', 'CS:Counseling Psychology:KRT:5', 'HP:Health Psychology:ANU:4', 'LAB:CA:Case Analysis:KAA:3', 'EDC:PS:Professional Skills:EDC:4', 'EDC:HRM:Human Resource Management:EDC:4']}
for j in subjects:
    l[j]=[]
    for k in subjects[j]:
        z=k.split(':')
        if(len(z)==4):
            l[j].append(subject(z[0],z[1],z[2],z[3],j,False))
        else:
            l[j].append(subject(z[1],z[2],z[3],z[-1],j,z[0]=="LAB"))


year=[]
for j in l:
    x=years(j)
    for k in l[j]:
        if k.year==j:
            x.subjects.append(k.name)
            x.instructors.append(k.instructor)
            if k.islab:
                x.lab=k
        
    year.append(x)

for i in year:
    lab_hours=i.lab.hours
    




# for i in l:
#     # print(i.name,i.instructor,i.hours)
#     p=np.array([i for _ in range(int(i.hours))],dtype=object)
#     d.append(p)


# d=np.array(d,dtype=object)
# it={1:[],2:[],3:[],4:[],5:[]}
# timetable={}
# for i in d:
#     for j in i:
#         it[j.year].append(j)     
# for i in it:
#     x=np.array(it[i])
#     np.random.shuffle(x)
#     p=x.reshape(6,5)
#     timetable[i]=p

# for q,w in timetable.items():
#     print(q,w)








