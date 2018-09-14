#a script to merge blast results from an unspecific ncbi blast and a blastdb created for a specific genome of interest.
import sys

dup_seq = open("duplicated_sequences.out", "w")
merged_seq = open("merged_blasts.out", "w")
with open (sys.argv[1]) as specific_hits, open (sys.argv[2]) as unspecific_hits:    
    header = {}    
    for seq in unspecific_hits:
#        print(seq.lstrip(">"))    
        seq_name = seq.lstrip(">").split('\t')[0]   
#        print(seq_name)
        header [seq_name] = seq
    for specific_seq in specific_hits:
        specific_name = specific_seq.lstrip(">").split('\t')[0]
#        print(specific_name)
        if specific_name in header:
#            print(specific_seq)
            dup_seq.write(specific_seq)
        else:
            header [specific_name] = specific_seq
    for key in header.keys():
        merged_seq.write(header[key])
    dup_seq.close()
    merged_seq.close()
