import csv


source_Adata_csv_array=[]
test_Adata_csv_array=[]
source=[]
destination=[]
test_Tdata={}
pairid=[]

Airport_to_available={}
solution={}



with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob1/Airlines Data CrowdStrike - RawTest_v5.csv') as csv_file:
    csv_Adata=csv.reader(csv_file)
    for row in csv_Adata:
        source.append(row[1])
        destination.append(row[2])
        source_Adata_csv_array.append(row)
#print(source_Adata_csv_array)
source=list(set(source))
destination=list(set(destination))

for  i in range(1,len(source)):
    for j in range(1,len(source_Adata_csv_array)):
        if(source[i]==source_Adata_csv_array[j][1]):
          Airport_to_available.setdefault(source[i],[]).append(source_Adata_csv_array[j][2])

print(Airport_to_available)


with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob1/testdata.csv') as csv_file:
    csv_Tdata=csv.reader(csv_file)
    for row in csv_Tdata:
        pairid.append(row[0])
        test_Adata_csv_array.append(row)
        test_Tdata[row[0]]=row[1],row[2]
#print(source_Adata_csv_array)

y=0
while(y<len(test_Adata_csv_array)//100):
 for case in test_Adata_csv_array[y:y+10000]:
    print(case)
    try:
      if (case[1] not in source):
                solution[case[0]]=-1
                
      elif(case[2] not in destination):
                solution[case[0]]=-1
                 

      elif(case[2] in Airport_to_available[case[1]]):
                solution[case[0]]=0
                

      casex=[x for x in Airport_to_available[case[1]]]
      print(casex)         

    except KeyError:
        solution[case[0]]=-1                             

 y=y+10000 
print(solution)     
print(len(solution))
del solution["PairID"]

with open('/home/chiraghs/my_codes/python/codestrike_hackhathon/prob1/solution.csv', mode='a+') as csv_file:
    fieldnames = ['PairID', 'Hops']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for k,v in solution.items():
        writer.writerow({'PairID': k, 'Hops': v})

"""
      else:
          for casex in Airport_to_available[case[1]]:       
              if(case[2] in Airport_to_available[casex]):
                    solution[case[0]]=1
                    break
              else:
                 for case_new in Airport_to_available[casex]:       
                    if(case[2] in Airport_to_available[case_new]):
                      solution[case[0]]=2
                      break
                    else:
                     for case_new1 in Airport_to_available[case_new]:       
                      if(case[2] in Airport_to_available[case_new1]):
                        solution[case[0]]=3
                        break
                      else:
                         for case_new2 in Airport_to_available[case_new1]:       
                           if(case[2] in Airport_to_available[case_new2]):
                              solution[case[0]]=4 
                              break 
                           else:
                             for case_new3 in Airport_to_available[case_new2]:       
                                if(case[2] in Airport_to_available[case_new3]):
                                  solution[case[0]]=5
                                  break
                                else:
                                   for case_new4 in Airport_to_available[case_new3]:       
                                       if(case[2] in Airport_to_available[case_new4]):
                                          solution[case[0]]=6
                                          break
                                       else:
                                            for case_new5 in Airport_to_available[case_new4]:       
                                               if(case[2] in Airport_to_available[case_new5]):
                                                 solution[case[0]]=7
                                                 break
                                               else:
                                                   for case_new6 in Airport_to_available[case_new5]:       
                                                     if(case[2] in Airport_to_available[case_new6]):
                                                       solution[case[0]]=8
                                                       
                                                     else:
                                                         solution[case[0]]=-1                                 
"""        