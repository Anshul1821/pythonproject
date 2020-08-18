import os,sys,csv,itertools
from itertools import combinations

path=os.getcwd()
sys.path.append(path)

csv_path=path + r"/dont_touch.csv"

with open(csv_path,newline='') as f:
    reader=csv.reader(f)
    data=list(reader)

department_list=[]

for i in data:
    for j in i:
        if j not in department_list:
            department_list.append(j)

all_combinations=[]

for r in range (len(department_list)+1):
    combinations_object = itertools.combinations(department_list, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list

results_dict={}
for student in data:
    for comb in all_combinations:
        count=[]
        for dept in comb:
            if dept in student:
                count.append("yes")
            else:
                count.append("no")
        if not "no" in count:
            if not comb in results_dict.keys():
                results_dict[comb] = 1
            else:
                results_dict[comb] += 1
           
[print(key, ":" ,value) for key,value in results_dict.items()]