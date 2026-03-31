#Import necessary package
import re
import matplotlib.pyplot as plt
from collections import defaultdict

#Initialise the stop codons
stop_codons = ["TAA", "TAG", "TGA"]

#Function 1: find the longest ORF in a sequence
def find_longest_orf(seq):
    start_codon = "ATG" #Initialise the start codon
    longest_orf = "" #Record the longest ORF

    #Find the start codon "ATG"
    atg_pos = -1 #Record the position of "ATG"
    for i in range(0, len(seq)-2):
        if seq[i:i+3] == start_codon:
            atg_pos = i
            break
    
    #From "ATG", check each codon if it == stop codon (check the bases by 3)
    if atg_pos != -1: #Make sure "ATG" exists
        for i in range(atg_pos, len(seq)-2, 3):
            codon = seq[i:i+3]
            #Found a stop codon, then record
            if codon in stop_codons:
                orf = seq[atg_pos:i+3] #The ORF from "ATG" to this stop codon
                if len(orf) > len(longest_orf): #Update the longest ORF
                    longest_orf = orf
                break
    
    if longest_orf == "":
        return None
    else:
        return longest_orf
    
#Function 2: read the fasta file and extract the sequence of each gene
def read_file(fasta_name):
    genes = [] #Record all sequences of genes
    crt_seq = "" #Record the current gene sequence

    fin = open(fasta_name, "r") #only read the file, so "r"
    for line in fin:
        line = line.strip() #Remove the newline character
            
        #Start with ">"  ->  this line is a new gene
        if re.search(r'^>', line):
            #If this is not the first gene, then we can find the sequence of the previous gene
            if crt_seq != "":
                genes.append(crt_seq) #Record the sequence of the previous gene
                crt_seq = "" #Reset the sequence for this new gene
        #Don't start with ">"  ->  this line is still sequence of the current gene
        else:
            #Add this line to the whole sequence
            crt_seq += line

        #Deal with the final gene alone (There is no new gene behind it, so we cannot use a next '>' to demonstrate it)
        if crt_seq != "":
            genes.append(crt_seq) #Record the sequence of the final gene

    fin.close() #Close the file
    return genes

#Function 3: count the number of codons in a sequence
def count_codons_in_orfs(orf_list, target_stop):
    #Record the number of codons in all ORFs
    codon_count = defaultdict(int) #a dictionary that can automatically set the value to 0 if the key does not exist

    #Check each ORF and count the codons
    for orf in orf_list:
        #Only count the ORFs that end with the target stop codon
        if not orf.endswith(target_stop):
            continue  #Skip this ORF if it does not end with the target stop codon, and move to the next ORF

        for i in range(0, len(orf)-2, 3):
            codon = orf[i:i+3]
            codon_count[codon] += 1 #Count the number of this codon
    
    return codon_count

#Function 4: draw the pie chart of codon usage
def draw_pie_chart(codon_count, target_stop):
    #Initialise the labels and values for the pie chart
    sorted_items = sorted(codon_count.items(), key=lambda x: -x[1])
    labels = [item[0] for item in sorted_items]
    values = [item[1] for item in sorted_items]

    #Draw the pie chart
    plt.figure(figsize=(16, 16), dpi=100)
    plt.pie(
        values,
        labels=labels,               
        labeldistance=1.05,          
        autopct='%1.1f%%',           
        pctdistance=0.75,            
        #rotatelabels=True,           
        textprops={'fontsize': 9}   
    )

    #Add title and save the figure
    plt.title(f"Codon Frequency (Stop Codon: {target_stop})", fontsize=16, pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f"codon_pie_{target_stop}.png")
    plt.close()



#The main function
if __name__ == "__main__":
    #Ask the user to input the target stop codon
    target_stop = input("Please input the target stop codon (TAA/TAG/TGA): ").rstrip().upper()

    #Read the fasta file and extract the sequence of each gene
    genes = read_file("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

    #Find the longest ORF in each gene and store them in a list
    longest_orfs = []
    for seq in genes:
        lorf = find_longest_orf(seq)
        if lorf:
            longest_orfs.append(lorf)

    #Count the number of codons in all longest ORFs
    codon_count = count_codons_in_orfs(longest_orfs, target_stop)

    #Print the codon count
    print(f"Codon count in longest ORFs with stop codon {target_stop}:")
    for codon, count in sorted(codon_count.items()):
        print(f"{codon}: {count}")

    #Draw the pie chart of codon usage
    draw_pie_chart(codon_count, target_stop)