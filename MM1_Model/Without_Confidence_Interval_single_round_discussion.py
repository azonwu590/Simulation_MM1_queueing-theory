import random as rnd
from math import *
import matplotlib.pyplot as plt

# generate arrival list
# generate departure list
# calculate waiting time
# generate confidence interval
# repeat several times of simulation

T = 500
Lmd = 5 #1,2,3,4,5
Miu = 4

arr = []
dep = []
st_list = []

t = 0
 #GENERATE ARRIVAL LIST
while(t <= T):
    arr.append(t)
    t += -(1/Lmd)*log(rnd.uniform(0,1))
    
#GENERATE DEPARTURE LIST
    #first person
#first person
st  = -(1/Miu)*log(rnd.uniform(0,1))
st_list.append(st)
dep.append(st)
j = 0


while( j + 1 < len(arr)): #j is index
    st = -(1/Miu)*log(rnd.uniform(0,1))
    st_list.append(st)
    if(dep[j] >= arr[j + 1]): 
        dep.append(dep[j]  + st)
    else:
        dep.append(arr[j + 1]  + st)
    j += 1

#CALCULATE WAITING TIME OF EACH PERSON BASED ON ARR AND DEP LIST
waiting_list = []
waiting_list.append(0) #first person
for i in range(1,len(arr)):
    wt = 0 if arr[i] >= dep[ i - 1] else dep[i - 1] - arr[i]
    waiting_list.append(wt)

### Output Discussion:
utilization = sum(st_list) / dep[ len(dep) - 1 ] #sum of service time / departure time of last customer
# Create a list of customer indices (i)
customer_indices = list(range(1, len(arr)+1)) #start from 1st customer

# Plot the waiting times
plt.bar(customer_indices, waiting_list)
plt.xlabel('Customer Index (i)')
plt.ylabel('Waiting Time(min)')
plt.title(f'Fixed_ending_time 500: Waiting Times for {len(arr)} Customers,lambda = {Lmd}, mu = {Miu}, utilization = {utilization} \n, expected waiting time = {sum(waiting_list)/ len(arr)}')
plt.grid(True)

# Show the plot
plt.show()


#debug
    # print(arr[len(arr) - 5:len(arr)])
    # print(dep[len(arr) - 5:len(arr)])
    # print(waiting_list[len(arr) - 5:len(arr)])
# print(len(arr))
