#pseudocode:
#define the initial variables: initial_infected, growth_rate, total_students, current_infected, day
#print the infected number on the 1st day
#while current_infected < total_students
#   day += 1
#   current_infected = current_infected + current_infected * growth_rate
#   print day + current_infected
#print day

#Initialise
initial_infected = 5
growth_rate = 0.4
total_students = 91
current_infected = initial_infected
day = 1

print(f"On day {day}, there are {current_infected} peoples infected.") #the output of the 1st day

#Do this until all the students are infected
while current_infected < total_students:
    day += 1 #a new day
    current_infected += current_infected * growth_rate #calculate the current infected number
    if current_infected >= total_students:
        print (f"On day {day}, there are {total_students} peoples infected.") #no more than 91 students
    else:
        print (f"On day {day}, there are {current_infected} peoples infected.") #the output of this day

print(f"It takes {day} days to infect all") #final days to infect all
