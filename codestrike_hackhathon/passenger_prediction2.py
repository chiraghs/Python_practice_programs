import csv

source_adata={}
country_name=[]
solutions={}
#t=[0,1,2,3,4,5,6,7]
#sumt=28
#sumt_square=140
#Number_of_quarters_given=8
# linear regression model y=mx+c
s_sq=[]
sum_sqt={}

with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob2/Training.csv') as csv_file:
    csv_source=csv.reader(csv_file)
    for row in csv_source:
        country_name.append(row[2])
        source_adata.setdefault(row[2],[]).append(row[3])

    for i in range(1,len(source_adata)):
        s=list(map(int,source_adata[country_name[i]]))
        sum_s=sum(s)
        t=0
        for j in s:
            s_sq.append(j*t)
            t=t+1
            sum_sqt[country_name[i]]=sum_s,sum(s_sq)
        for elem in range(len(s_sq)):
            s_sq.pop()
    #print(sum_sqt)        

    for i in range(1,len(source_adata)):        
        #print(sum_sqt[country_name[i]][1],sum_sqt[country_name[i]][0])
        m=(8*int(sum_sqt[country_name[i]][1]) - 28*int(sum_sqt[country_name[i]][0]))/(8*140-784)
        c=(sum_sqt[country_name[i]][0]-m*28)/8
        #print(country_name[i],m,c)
        solutions[country_name[i]]=round(abs(m*8+c))
        
        

with open('/home/chiraghs/my_codes/python/codestrike_hackhathon/prob2/solution.csv',mode='a+') as csv_file:
    fieldnames=['COUNTRY_NAME','PASSENGERS_TO_INDIA']

    writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    for k,v in solutions.items():
        writer.writerow({'COUNTRY_NAME': k, 'PASSENGERS_TO_INDIA': v})

print(solutions)        