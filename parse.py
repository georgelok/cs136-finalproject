def parse(file) :
    bids = []
    atoms = []
    with open(file,'r') as f:
        lines = f.readlines()
        num_goods = (lines[20].split(' ')[1].strip())
        num_bids = (lines[21].split(' ')[1].strip())
        num_dummy = int(lines[22].split(' ')[1].strip())
        for line in lines[24:] :
            fields = [field.strip() for field in line.split('\t')]
            bids.append(float(fields[1]))
            atoms.append([int(i) for i in fields[2:-1]])
    return (num_goods, num_bids, num_dummy, bids, atoms)


def filterAtoms(num_goods, max_size, atoms)


print parse('100_100-0000.txt')