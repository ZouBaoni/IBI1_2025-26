a = 5.08 #the estimated population in Scotland (million) in 2004
b = 5.33 #the estimated population in Scotland (million) in 2014
c = 5.55 #the estimated population in Scotland (million) in 2024
d = b - a #the change in population between 2014 and 2004
e = c - b #the change in population between 2024 and 2014

#print d and e
print ("d = " + str(d))
print ("e = " + str(e))

#compare d to e and output
if d > e:
    print ("d > e") 
else:
    print ("d <= e")

#d is larger
#the population growth is decelerating in Scotland

X = True #initialise X
Y = False #initialise Y
W = X or Y #calculate the result

print ("W = " + str(W)) #output for the result

#the truth table for W
# X     Y     W(X or Y)
# True  True  True
# True  False True
# False True  True
# False False False