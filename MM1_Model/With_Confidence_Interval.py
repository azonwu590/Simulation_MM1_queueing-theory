import random as rnd
from math import *
import matplotlib.pyplot as plt
import numpy as np
# set a lambda and Miu
    # set a num_simulation
        # generate arrival list
        # generate departure list
        # calculate average waiting time(mean)
        # store into a list: mean_list
    # gen mean of mean, confident interval

def mm1_cal_wt(in_lamda, in_miu):
    T = 500
    Lmd = in_lamda
    Miu = in_miu

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

    return sum(waiting_list)/ len(arr)


NUM_SIM = 10 # try 10, 60, 250
miu_list = [0.5,0.75,1]
lamda_list = np.arange(0.1, 1.01, 0.01) 
moml = [[],[],[]]
cil = [[],[],[]] 
for m, miu in enumerate(miu_list):
    for l, lamda in enumerate( lamda_list ):
        mean_wts = []
        for s in range(NUM_SIM):
            mean = mm1_cal_wt( lamda, miu ) #mm1_cal_wt:a function that simulates a single round of mm1 and returns the average waiting time (mean)
            mean_wts.append(mean) # mean_wts: a list of mean Xi
        mean_wts = np.array(mean_wts) 
        moml[m].append(np.mean(mean_wts)) # moml (mean of mean list): a list of mean of mean: add one element for one lamda, miu pair that's gone through NUM_SIM of simulation
        cil[m].append( 1.96 * sqrt(np.var(mean_wts, ddof=1))/sqrt(NUM_SIM)) #np.var(mean_wts, ddof=1) is the sample variance, cil is the  list of (1.96 * sample_std/ n-1)

moml = np.array(moml)
cil = np.array(cil)
# Plot the lines on the same plot
plt.plot(lamda_list, moml[0] , label='miu = 0.5')
plt.fill_between(lamda_list, moml[0] - cil[0], moml[0] + cil[0], color='gray', alpha=0.3)
plt.plot(lamda_list, moml[1] , label='miu = 0.75')
plt.fill_between(lamda_list, moml[1] - cil[1], moml[1] + cil[1], color='purple', alpha=0.3)
plt.plot(lamda_list, moml[2] , label='miu = 1')
plt.fill_between(lamda_list, moml[2] - cil[2], moml[2] + cil[2], color='green', alpha=0.3)

# Add labels and a legend
plt.xlabel('lambda')
plt.ylabel('average waiting time')
plt.title(f'{NUM_SIM} simulation, ending time = 500')

# Add legend
plt.legend()

# Show the plot
plt.show()



