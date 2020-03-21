import csv

source = dict(list())
destination = dict(list())
pairid = dict()
hobs = dict()

def search(lst,element):
    for q in lst:
        if q == element:
            return True
    return False

with open(r'/home/chiraghs/Downloads/crowdstrike/Airlines Data CrowdStrike - RawTest_v5.csv') as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader2:
        if line_count == 0:
            line_count = 1
            continue
        
        if destination.get(row[2]):
            destination[row[2]].append(row[1])
        else:
            destination[row[2]] = [row[1]]
        
        if source.get(row[1]):
            source[row[1]].append(row[2])
        else:
            source[row[1]] = [row[2]]
        

print(source)
print(destination)


with open(r'/home/chiraghs/Downloads/crowdstrike/testdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count = 1
            continue
        pairid[row[0]] = [row[1],row[2]]
i = 0
j = 0
for k,v in pairid.items():
    try:
        if search(source[v[0]],v[1]):
            hobs[k] = 0
            j+=1
        else:
            for w in source[v[0]]:
                if search(destination[v[1]],w):
                    hobs[k] = 1
                    j+=1
                    break
    except KeyError:
        i +=1

print(j)
del hobs["PairID"]

with open('/home/chiraghs/Downloads/crowdstrike/solution.csv', mode='a+') as csv_file:
    fieldnames = ['PairID', 'Hops']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for k,v in hobs.items():
        writer.writerow({'PairID': k, 'Hops': v})