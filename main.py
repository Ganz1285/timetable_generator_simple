import sqlite3
import numpy as np
from numpy import random
import itertools

con=sqlite3.connect("try.db")


def subjects():
    subjects = [[], [], [], [], []]
    for i in range(5):
        for row in cur.execute(f"SELECT subject_id,staff_id,hours FROM subjects WHERE year=={i+1};"):
            subjects[i].append(str(row[0]+':'+row[1]+":"+str(row[2])))

    return(subjects)




def time_table():
    table={1:{},2:{},3:{},4:{},5:{},6:{}}
    
    
    
    return ""

if __name__ =="__main__":
    cur=con.cursor()
    sub=subjects()
    d={}
    j=1
    
    
    for i in sub:
        l=np.array([j for j in i for _ in range(int(j[-1]))])
        np.random.shuffle(l)
        d[j]=l.reshape(6,5)
        j+=1
    print(d)
    # for i in set(l):
    #     print(i,l.count(i))
    #     print(i,np.count_nonzero(b==i))
    # arr0=[1,2,3,4]
    # arr2=[5,6,7,8]
    # arr3=[1,4,5,2]
    # arr=[arr0,arr2,arr3]
    # lens=[len(a)for a in arr]
    # print("lens:",lens)
    # p=[.5,.1,.4]
    # new_arr=np.concatenate(arr)
    # print("new_rr:",new_arr)
    # new_p=np.repeat(np.divide(p,lens),lens)
    # # for i in sub:
    # print("new_p:",new_p)
    # x=np.random.choice(new_arr, p=new_p,size=(5,3))
    # print(x)
    #     print([int((k[-1]))/30 for k in i])
    #     d[j]=random.choice(np.array(i),(6,5), 1,p=np.array([int((k[-1]))/30 for k in i]))
    #     j+=1
    #     break
    # for j in set(x):
    #     f=[np.count_nonzero(x == j)/len(x)]
    #     print(j,np.count_nonzero(x == j),f)
    # for i in set(x):
    #     print(i,np.count_nonzero(x == i))
    # print("--")
    # it={}
    # for i in t:
    #     if i not in it.keys():
    #         it[i]=1
    #     else:
    #         it[i]+=1
    # print(it)
    # print(it)
    #     print(j,":",k)
    # for i in sub:
    #   
    #   print(f"{i}th year subjects:",*sub[i])
        