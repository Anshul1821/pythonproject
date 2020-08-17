work1=open("list1.txt","r")
list1=[]
for item in work1:
    list1.append(item)
  
work2=open("list2.txt","r")
list2=[]
for item in work2:
    list2.append(item)

work3=open("list3.txt","r")
list3=[]
for item in work3:
    list3.append(item)


list_of_departments=["Content and Editorial","Creativity","Design and Video","Event Management and Publicity",
"Technical","Social Media Management","Public Relations","Photography"]
list=[]
'''
The link has 8 departments. Sample result of your code can be:

EM + Tech = 8 people. Which means only 8 students have applied for both EM and Tech
Em + tech + Design = 4 people. Which means only 4 people have applied for all these 3 departments.

This is just an example, you gotta find all the combinations of 2 and 3. Please text me if you have any doubt.        
'''
for i in range(7):
    for j in range(1,8):
        num=0
        list=[list_of_departments[i],list_of_departments[j]]
        print(list)
        for k in range(118):
            if ([list1[k],list2[k]] or [list2[k],list3[k]] or [list1[k],list3[k]])==list:
                num=num+1; 
            print(num)    