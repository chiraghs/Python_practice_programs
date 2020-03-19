import csv

Depart=[]
Arrive=[]
schedule_name=[]

source_1data={}
source_1half={}

source_2data={}
source_2half={}

source_3data={}
source_3half={}

source_4data={}
source_4half={}

source_5data={}
source_5half={}

source_6data={}
source_6half={}

source_7data={}
source_7half={}

source_8data={}
source_8half={}

source_9data={}
source_9half={}

source_10data={}
source_10half={}

source_11data={}
source_11half={}


source_12data={}
source_12half={}



with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob3/train.csv') as csv_file:
    csv_source=csv.reader(csv_file)
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    i10=0
    i11=0
    i12=0
    for row in csv_source:
        if(row[6]=='1'):
                i1=i1+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i1))
                source_1data[("schedule1_"+str(i1))]=row[1],row[2],row[3]
                source_1half[("schedule1_"+str(i1))]=row[1],row[2]
        if(row[6]=='2'):
                i2=i2+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i2))
                source_2data[("schedule2_"+str(i2))]=row[1],row[2],row[3]
                source_2half[("schedule2_"+str(i2))]=row[1],row[2]
        if(row[6]=='3'):
                i3=i3+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i3))
                source_3data[("schedule3_"+str(i3))]=row[1],row[2],row[3]
                source_3half[("schedule3_"+str(i3))]=row[1],row[2]
        if(row[6]=='4'):
                i4=i4+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i4))
                source_4data[("schedule4_"+str(i4))]=row[1],row[2],row[3]
                source_4half[("schedule4_"+str(i4))]=row[1],row[2]
        if(row[6]=='5'):
                i5=i5+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i5))
                source_5data[("schedule5_"+str(i5))]=row[1],row[2],row[3]
                source_5half[("schedule5_"+str(i5))]=row[1],row[2]
        if(row[6]=='6'):
                i6=i6+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i6))
                source_6data[("schedule6_"+str(i6))]=row[1],row[2],row[3]
                source_6half[("schedule6_"+str(i6))]=row[1],row[2]
        if(row[6]=='7'):
                i7=i7+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i7))
                source_7data[("schedule7_"+str(i7))]=row[1],row[2],row[3]
                source_7half[("schedule7_"+str(i7))]=row[1],row[2]
        if(row[6]=='8'):
                i8=i8+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i8))
                source_8data[("schedule8_"+str(i8))]=row[1],row[2],row[3]
                source_8half[("schedule8_"+str(i8))]=row[1],row[2]
        if(row[6]=='9'):
                i9=i9+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i9))
                source_9data[("schedule9_"+str(i9))]=row[1],row[2],row[3]
                source_9half[("schedule9_"+str(i9))]=row[1],row[2]
        if(row[6]=='10'):
                i10=i10+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i10))
                source_10data[("schedule10_"+str(i10))]=row[1],row[2],row[3]
                source_10half[("schedule10_"+str(i10))]=row[1],row[2]
        if(row[6]=='11'):
                i11=i11+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i11))
                source_11data[("schedule11_"+str(i11))]=row[1],row[2],row[3]
                source_11half[("schedule11_"+str(i11))]=row[1],row[2]
        if(row[6]=='12'):
                i12=i12+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule_"+str(i12))
                source_12data[("schedule12_"+str(i12))]=row[1],row[2],row[3]
                source_12half[("schedule12_"+str(i12))]=row[1],row[2]

#for i in range(len(source_1data)):
for j in ['source_'+str(i)+'data' for i in range(13)]:
    print(len(j))