"""
Import libraries
Define parameters: N, S, I, R, beta, gamma, time_steps
Create empty lists: S_list, I_list, R_list
Append initial S, I, R to the lists

FOR t FROM 1 TO time_steps:
    # Infection step
    infection_prob = beta * (I / N)
    new_infected = number of S that get infected (random by infection_prob)

    # Recovery step
    new_recovered = number of I that recover (random by gamma)

    # Update
    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered

    # Save to history
    append S to S_list
    append I to I_list
    append R to R_list

Plot S_list, I_list, R_list against time
Add labels, legend, title
Save the figure
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Define the basic variables for the SIR model
N = 10000  # Total population
I = 1    # Initial number of infected individuals
R = 0    # Initial number of recovered individuals
S = N - I - R  # Initial number of susceptible individuals
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 1000  # Number of time steps

#Create empty lists to store the history of S, I, R
S_list = [S]
I_list = [I]
R_list = [R]

#The main loop for the SIR model simulation
for i in range(time_steps):
    #Calculate the probability of infection
    infection_prob = beta * (I / N)
    
    #S --> I (1 = infected, 0 = not infected)
    infect_flags = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]) #return a list (n=S)
    new_infected = np.sum(infect_flags)

    #I --> R (1 = recover, 0 = not recover)
    recover_flags = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
    new_recovered = np.sum(recover_flags)

    #Update the counts of S, I, R
    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered

    #Append the current values to the history lists
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)


#Plotting the results
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR.png')
plt.show()