with open('all_seqs.fasta') as infile:
    new_dict = {}
    prev = ''
    for l in infile:
        line = l.rstrip('\n')
        if line.startswith(">"):
            k = line.lstrip('>')[:4] # to just get first 4 of acc num
            new_dict[k] = []
            prev = k
        else:
            new_dict[prev] = line

print(new_dict)
