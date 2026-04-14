"""
IMPORT libraries

CREATE a 100x100 grid, all zeros (0 = susceptible)
CHOOSE a random position, set it to 1 (infected)

SET beta = 0.3, gamma = 0.05
SET time_steps = 100

FOR each time step:
    FIND all coordinates where grid == 1 (infected)
    
    # Infection process
    FOR each infected cell:
        CHECK all 8 neighboring cells
        FOR each neighbor:
            IF neighbor is 0 AND random < beta:
                mark neighbor to be infected

    # Recovery process
    FOR each infected cell:
        IF random < gamma:
            mark cell to be recovered

    APPLY all infections and recoveries
    PLOT the grid as a heatmap
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Make a 2D array of all susceptible population (100x100)
population = np.zeros((100, 100))

#Randomly infect one individual as the initial infected case
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

#Plot the initial state of the population (with heatmap)
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', vmin=0, vmax=2,interpolation='nearest')

#Define the basic variables for the SIR model
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
time_steps = 100  # Number of time steps

neighbors = [(-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0), (1,1)]

#The main loop for the SIR model simulation
for step in range(time_steps):
    new_population = population.copy() #Create a copy of the grid to apply updates simultaneously
    infected = list(zip(*np.where(population == 1))) #Find all coordinates of infected individuals

    for i, j in infected:
        #Infection process
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 100 and 0 <= nj < 100: #Check boundaries
                if population[ni, nj] == 0 and np.random.rand() < beta: #Infect neighbor with probability beta
                    new_population[ni, nj] = 1

        #Recovery process
        if np.random.rand() < gamma: #Recover with probability gamma
            new_population[i, j] = 2

    population = new_population #Update the population grid

    #Plot the current state of the population (with heatmap)
    if step % 5 == 4: #Plot every 5 steps
        plt.clf() #Clear the previous plot
        plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
        plt.title(f"Spatial SIR - Step {step+1}")
        plt.pause(0.1)

plt.savefig("spatial_SIR_final.png")
plt.show()