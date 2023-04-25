with open('all_seqs.fasta') as infile:
    total = 0
    new_dict = {}
    prev = ''
    for l in infile:
        line = l.rstrip('\n')
        if line.startswith(">"):
            # k = line.lstrip('>')[:4]  # to just get first 4 of acc num
            k = line.lstrip()
            new_dict[k] = []
            prev = k
        else:
            new_dict[prev] = line
            total += 1

new_file = open('new_seqs.fasta', 'w')
count = 0
seen = []
for x in new_dict:
    if len(new_dict[x]) <= 200:
        # if True:
        if new_dict[x][:20] not in seen:
            new_file.write(f"{x}\n{new_dict[x]}\n")
            print(f"{x}: {new_dict[x]}")
            count += 1
            seen.append(new_dict[x][:20])

print(f"count: {count}")
print(f"total: {total}")
