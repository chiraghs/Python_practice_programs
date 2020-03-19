import csv

source_adata={}
country_name=[]
solutions={}

with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob2/Training.csv') as csv_file:
    csv_source=csv.reader(csv_file)
    for row in csv_source:
        country_name.append(row[2])
        source_adata.setdefault(row[2],[]).append(row[3])

    for i in range(1,len(source_adata)):
        s=list(map(int,source_adata[country_name[i]]))
        print(country_name[i],sum(s)//8)
        solutions[country_name[i]]=sum(s)//8

with open('/home/chiraghs/my_codes/python/codestrike_hackhathon/prob2/solution.csv',mode='a+') as csv_file:
    fieldnames=['COUNTRY_NAME','PASSENGERS_TO_INDIA']

    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for k,v in solutions.items():
        writer.writerow({'COUNTRY_NAME': k, 'PASSENGERS_TO_INDIA': v})