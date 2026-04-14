"""
Import numpy as np
Import matplotlib.pyplot as plt

Set N = 10000
Set beta = 0.3, gamma = 0.05
Set time_steps = 1000

Create a list of vaccination rates: [0, 0.1, 0.2, ..., 1]

for each vacc_rate in vaccination rates:
    Set I = 1
    Set V = N * vacc_rate (integer)
    Set S = N - I - V
    Set R = 0

    Create I_list to store infected numbers
    Append initial I to I_list

    for t IN 1 TO time_steps:
        infection_prob = beta * (I / N)
        new_infected = random infected from S
        new_recovered = random recovered from I

        S = S - new_infected
        I = I + new_infected - new_recovered
        R = R + new_recovered

        append I to I_list

    Plot I_list with label showing vacc_rate

Add labels, legend, title, grid
Save the figure
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Define the basic (unchanged) variables for the SIR model
N = 10000  # Total population
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 1000  # Number of time steps

#Create a list of vaccination rates
vaccination_rates = np.arange(0, 1.1, 0.1)  # From 0 to 1 with step of 0.1

plt.figure(figsize=(8, 5), dpi=150)

#Loop through each vaccination rate
for vacc_rate in vaccination_rates:
    I = 1  # Initial number of infected individuals
    V = int(N * vacc_rate)  # Number of vaccinated individuals
    S = N - I - V  # Initial number of susceptible individuals
    R = 0  # Initial number of recovered individuals

    I_list = [I]  # List to store the history of infected numbers

    #The main loop for the SIR model simulation
    for i in range(time_steps):
        new_infected = 0
        new_recovered = 0
        
        #S --> I (1 = infected, 0 = not infected)
        if S > 0:
            infection_prob = beta * (I / N)
            infect_flags = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
            new_infected = np.sum(infect_flags)
        
        #I --> R (1 = recover, 0 = not recover)
        if I > 0:
            recover_flags = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
            new_recovered = np.sum(recover_flags)

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        S = max(S, 0)  # Ensure S does not go negative
        I = max(I, 0)  # Ensure I does not go negative
        R = max(R, 0)  # Ensure R does not go negative

        I_list.append(I)

    #Draw the plot for the current vaccination rate
    color = cm.viridis(vacc_rate)  # Get a color from the colormap based on vaccination rate
    plt.plot(I_list, color=color, label=f'{vacc_rate*100:.0f}%')


plt.xlabel('time')
plt.ylabel('number of infected individuals')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('SIR_vaccination.png')
plt.show()