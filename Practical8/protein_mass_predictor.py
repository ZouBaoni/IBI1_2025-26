#Define the function
def calculate_protein_mass(protein_sequence):
    """
    Calculate the mass of a protein sequence based on the masses of its constituent amino acids.
    Input: A string representing a protein sequence (composed of single-letter amino acid codes).
    Output: A float representing the total mass of the protein sequence.
        (If the input contains characters that are not valid amino acid codes, the function will report an error message and return None.)
    """

    # Initialise a dictionary for the amino acid masses
    amino_acid_masses = {
        'G': 57.02,  # Glycine
        'A': 71.04,  # Alanine
        'S': 87.03, # Serine
        'P': 97.05, # Proline
        'V': 99.07, # Valine
        'T': 101.05, # Threonine
        'C': 103.01, # Cysteine
        'I': 113.08, # Isoleucine
        'L': 113.08, # Leucine
        'N': 114.04, # Asparagine
        'D': 115.03, # Aspartic acid
        'Q': 128.06, # Glutamine
        'K': 128.09, # Lysine
        'E': 129.04, # Glutamic acid
        'M': 131.04, # Methionine
        'H': 137.06, # Histidine
        'F': 147.07, # Phenylalanine
        'R': 156.10, # Arginine
        'Y': 163.06, # Tyrosine
        'W': 186.08, # Tryptophan
    }
    
    total_mass = 0 #Store the total mass of the protein sequence
    
    #Check all AAs in the input sequence and add their masses to the total mass
    for aa in protein_sequence:
        if aa in amino_acid_masses.keys():
            total_mass += amino_acid_masses[aa]
        else:
            #If the input contains characters that are not valid amino acid codes, report an error message and return None
            print(f"Error: '{aa}' is not a valid amino acid code.")
            return None
    #Output the total mass of the protein sequence
    return total_mass


#The main function to test the calculate_protein_mass function
if __name__ == "__main__":
    #A sample protein sequence
    sequence = "ACDEFGHIKLMNPQRSTVWY"
    mass = calculate_protein_mass(sequence)

    if mass is not None:
        print(f"The mass of the total protein sequence '{sequence}' is: {mass:.2f} amu.")
    