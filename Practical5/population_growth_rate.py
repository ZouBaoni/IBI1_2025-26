#Create a dictionary to store the 2 population data of each country
#dictionary structure: 'country': [population_2020, population_2024]
pop = {'UK': [66.7, 69.2],
       'China': [1426, 1410],
       'Italy': [59.4, 58.9],
       'Brazil': [208.6, 212.0],
       'USA': [331.6, 340.1]}

#Create a dictionary to store each absolute population change
#dictionary structure: 'country': pop_change
pop_change = {}
#Process each country
for country, [pop_20, pop_24] in pop.items():
    pop_change[country] = round(pop_24 - pop_20, 1) #calculate the absolute population change
    percent_change = round((pop_24 - pop_20) / pop_20 * 100, 2) #calculate the percentage change
    print(f"The percentage population change of {country} is {percent_change}%.") #print the percent_change

#Create a list to sort the abosolute changes in pop_change
sorted_pop_change = list(pop_change.values()) #initialise the list as values in pop_change
sorted_pop_change.sort() #sort the list from the smallest to the largest
sorted_pop_change.reverse() #make the list sorted from the largest to the smallest
#print the sorted change
print(f"Sort the population changes from the largest increase to the largest decrease: {sorted_pop_change}") 

#Find the countries	with the largest increase and the largest decrease in population
max_country = max(pop_change, key=pop_change.get) 
min_country = min(pop_change, key=pop_change.get)
#Print the results
print(f"The country with the largest increase is {max_country}.")
print(f"The country with the largest decrease is {min_country}.")

#Import Python packages used for 2D graphics
import matplotlib.pyplot as plt
import numpy as np

#Necessary information for the bar chart
countries = list(pop_change.keys())
changes = list(pop_change.values())
#Create the bar chart (use countries, changes; set width, color)
bars = plt.bar(countries, changes, width=0.6, color=['lightgreen','lightcoral','lightcoral','lightgreen','lightgreen'])
plt.title("The population change for each country") #add title
plt.xlabel("Country") #add x label
plt.ylabel("Absolute population change (Million)") #add y label
plt.grid(axis='y', linestyle='--', alpha=0.5) #add grid line on y axis
plt.bar_label(bars, fmt='%.1f') #label the specific number
#Show the bar chart
plt.show()