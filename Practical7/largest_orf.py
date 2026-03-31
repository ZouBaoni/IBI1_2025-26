#Initialise the mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#a set to store 3 stop codons
stop_codons = {"UAA", "UAG", "UGA"}
#store all ORFs
all_orfs = []

#Determine whether the start codon exists
if not 'AUG' in seq:
    print("No ORF")
#start codon exist -> ORF exist
else:
    #check all codons to find the first start codon 'AUG'
    for i in range(0, len(seq)-2):
        #extract the current codon
        codon = seq[i:i+3]

        if codon == 'AUG':
            #From now, read 3 bases at a time (3 bases = 1 condon), until we find the stop codon
            for j in range(i+3, len(seq)-2, 3):
                c_codon = seq[j:j+3]
                #Determine if this codon is stop codon
                if c_codon in stop_codons:
                    #Store the sequence
                    orf = seq[i:j+3]
                    all_orfs.append(orf)
                    #the ORF ends at the first stop codon
                    break
        
#find the largest ORF (in length)
largest_orf = max(all_orfs, key=len)
#Outputs
if largest_orf == '':
    print('No ORF')
else:
    print(f"The largest ORF: {largest_orf}")
    print(f"The length of the largest ORF: {len(largest_orf)} nucleotides")

