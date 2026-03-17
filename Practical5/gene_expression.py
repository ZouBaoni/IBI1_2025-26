#Create a dictionary (genes + expression values)
genes = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3, 'ESR1':10.7}
print (genes) #print the dictionary
genes['MYC'] = 11.6 #Add 'MYC':11.6 to the dictionary

#Import Python packages for 2D graphics
import matplotlib.pyplot as plt
import numpy as np

#Draw the bar chart
names = list(genes.keys()) #prepare for the x axis locations (gene names)
expressions = list(genes.values()) #prepare for the corresponding height (expression values)
bars = plt.bar(names, expressions, width=0.6, color='skyblue')
#Create the bar chart (use names, expressions to input the core parameters of the function; set width and color)
plt.title("Expression Levels of Different Genes") #add the title
plt.xlabel("Gene names") #add x label
plt.ylabel("Expression level") #add y label
plt.grid(axis='y', linestyle='--', alpha=0.5) #add grid line
plt.bar_label(bars, fmt='%.1f') #add specific numbers
#Show the bar chart
plt.show() 

#Define target_gene to store the name of the gene of interest
target_gene = 'TP53'
#Determine whether the gene is in the dataset
if target_gene in genes:
    print(target_gene + ": " + str(genes[target_gene])) #if exists, print the expression value
else:
    print("Error. The targeted gene is not in the dataset!") #if not exists, print the error message

sum = 0 #store the sum of gene expression
len = len(genes) #store the number of items in genes
for value in genes.values():
    sum += value #add each value in genes to sum
avg = round(sum / len, 2) #calculate the average expression level
print("average gene expression level across all genes: " + str(avg)) #print the result