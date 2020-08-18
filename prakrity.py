work1=open("list1.txt","r")
list1=[]
for item in work1:
    items=item.strip()
    list1.append(items)
print(list1)  
work2=open("list2.txt","r")
list2=[]
for item in work2:
    items=item.strip()
    list2.append(items)

work3=open("list3.txt","r")
list3=[]
for item in work3:
    items=item.strip()
    list3.append(items)


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
    for j in range(i+1,8):
        num=0
        list=[list_of_departments[i],list_of_departments[j]]
        print(list)
        for k in range(118):
            a=[list1[k],list2[k]]
            b=[list1[k],list3[k]] 
            c=[list2[k],list3[k]]
            if (a or b or c)==list:
                num=num+1
        print(num)               