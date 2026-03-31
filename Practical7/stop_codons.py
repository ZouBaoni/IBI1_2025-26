#Import necessary package
import re

#Open the files
fin = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") #only read the original file
fout = open("stop_genes.fa", "w") #create a file for output + write

#Initialise the stop codons
stop_codons = ["TAA", "TAG", "TGA"]
#Store the current gene name and sequence
crt_gene = "" #the first line of each gene
crt_seq = "" #the rest lines

#Read the file line by line
for line in fin:
    #Remove the "\n" at the last of each line
    line = line.rstrip()

    #Determine whether this line contains a new gene
    #Start with ">"   ->   new gene
    if re.search(r'^>', line):
        #We find a new gene, which means the last gene has already ended, so we can operate with it
        #Check whether the last gene exists
        if crt_gene != "" and crt_seq != "":
            
            #Find the start codon "ATG"
            atg_pos = -1 #Record the position of "ATG"
            for i in range(0, len(crt_seq)-2):
                if crt_seq[i:i+3] == "ATG":
                    atg_pos = i
                    break
            
            #From "ATG", check each codon if it == stop codon (check the bases by 3)
            find_codon = ""
            if atg_pos != -1: #Make sure "ATG" exists
                for i in range(atg_pos, len(crt_seq)-2, 3):
                    codon = crt_seq[i:i+3]
                    #Found a stop codon, then record
                    if codon in stop_codons:
                        find_codon = codon
                        break
            
            #If ORF (both start and stop codons) exists, then record the gene name
            if find_codon != "":
                gene_name = re.search(r'^>(\S+)\s', crt_gene).group(1)
                #Print the gene name and stop codon
                fout.write(f">{gene_name}; {find_codon}\n")
                #Print the sequence
                fout.write(crt_seq + "\n")
        
        #Start dealing with the new gene
        crt_gene = line #Now line start with ">", it is the new gene
        crt_seq = ""


    #Don't start with ">"  ->  this line is still sequence of the current gene
    else:
        #Add this line to the whole sequence
        crt_seq += line


#Deal with the final gene alone (There is no new gene behind it, so we cannot use a next '>' to demonstrate it)
#The code is same as above
if crt_gene != "" and crt_seq != "":
    #Find the start codon "ATG"
    atg_pos = -1 #Record the position of "ATG"
    for i in range(0, len(crt_seq)-2):
        if crt_seq[i:i+3] == "ATG":
            atg_pos = i
            break
    #From "ATG", check each codon if it == stop codon (check the bases by 3)
    find_codon = ""
    if atg_pos != -1: #Make sure "ATG" exists
        for i in range(atg_pos, len(crt_seq)-2, 3):
            codon = crt_seq[i:i+3]
            #Found a stop codon, then record
            if codon in stop_codons:
                find_codon = codon
                break
    #If ORF (both start and stop codons) exists, then record the gene name
    if find_codon != "":
        gene_name = re.search(r'^>(\S+)\s', crt_gene).group(1)
        #Print the gene name and stop codon
        fout.write(f">{gene_name}; {find_codon}\n")
        #Print the sequence
        fout.write(crt_seq + "\n")


#Close the files
fin.close()
fout.close()