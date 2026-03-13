#pseudocode:
#define and initialise variables: age, weight, gender, creatine
#define: valid = True
#check the inputs: if any variables do not meet the requirements, then let valid = False
#meanwhile, use a string "error" to record which variable is wrong
#if valid = True: 
#   calculate CrCl
#   print
#else
#   print which variable is wrong?

#define and initialise the variables
age = 50
weight = 60
gender = "male"
creatine = 80
#initialise the two variables to record if the data is valid
valid = True
error = "Error. The inputs are invalid. You should correct:"

#check all the variables
if age >= 100:
    valid = False
    error += " age"

if weight <= 20 or weight >= 80:
    valid = False
    error += " weight"

if gender != "male" and gender != "female":
    valid = False
    error += " gender"

if creatine <= 0 or creatine >= 100:
    valid = False
    error += " creatine"

#if the data is valid, calculate CrCl
if valid:
    #determine the constant x
    if gender == "male":
        x = 1
    elif gender == "female":
        x = 0.85
    #calculate the result and output
    CrCl = (140 - age) * weight / (72 * creatine) * x
    print (f"CrCl = {CrCl}ml/min")
#if the data is invalid, print the error
else:
    print(error)
