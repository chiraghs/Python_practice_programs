import csv

source_Adata={}
source=[]
destination=[]
test_Tdata={}
pairid=[]
solution={}


with open(r'/home/chiraghs/Downloads/crowdstrike/Airlines Data CrowdStrike - RawTest_v5.csv') as csv_file:
    csv_Adata=csv.reader(csv_file)
    L_Adata=0
    for row in csv_Adata:
        source.append(row[1])
        destination.append(row[2])
        source_Adata[L_Adata]=row[1],row[2]
        L_Adata=L_Adata+1

    #print(destination)


with open(r'/home/chiraghs/Downloads/crowdstrike/testdata.csv') as csv_file:
    csv_Tdata=csv.reader(csv_file)
    for row in csv_Tdata:
        pairid.append(row[0])
        test_Tdata[row[0]]=row[1],row[2]


    #print(test_Tdata[pairid[1048576]][0])
   # print(len(pairid))



    for i in range(len(test_Tdata)//100):
        for j in range(len(source_Adata)):
            if (test_Tdata[pairid[i]][0] not in source):
                solution[pairid[i]]=-1
            elif(test_Tdata[pairid[i]][1] not in destination):
                solution[pairid[i]]=-1

    print(solution)            