#Create a list to store all the heart rates
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
total_number = len(heart_rates) #get the number of patients
avg_rate = round(sum(heart_rates) / total_number, 2) #calculate the average rate
print(f"There are {total_number} patients in the dataset. The mean heart rate is {avg_rate}.") #output

low = 0 #store the number of patients whose heart rate is low
normal = 0 #store the number of patients whose heart rate is normal
high = 0 #store the number of patients whose heart rate is high
#Determine the category for each patient and count
for rate in heart_rates:
    if rate < 60:
        low += 1
    elif rate > 120:
        high += 1
    else:
        normal += 1
print(f"Number of the patients whose heart rates are low: {low}.") #output low
print(f"Number of the patients whose heart rates are normal: {normal}.") #output normal
print(f"Number of the patients whose heart rates are high: {high}.") #output high
#Find the max
category = {'low':low, 'normal':normal, 'high':high} #create a dictionary to connect the categories and numbers
max_category = max(category, key=category.get) #find the max category
print(f"The {max_category} category contains the largest number of patients.") #output

#Import Python packages for 2D graphics
import matplotlib.pyplot as plt
import numpy as np

#Necessary data for the pie chart
labels = ['Low', 'Normal', 'High']
sizes = [low, normal, high] #the initial number
colors = ["lightgreen", "lightcoral", "lightskyblue"]
#Define a function to show both percentages and initial numbers
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{pct:.1f}%\n({val:d} people)'
    return my_autopct
#Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct=make_autopct(sizes))
plt.axis('equal') #ensure the pie is a circle
plt.title("Distribution of heart rate categories") #add title
#Show the pie chart
plt.show()