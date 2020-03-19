import csv
import re
import string
from math import radians, sin, cos, acos

Depart=[]
Arrive=[]
schedule_name=[]

source_1data={}          #schedule_ info of month num 1


latlong={}           #latlaong of individual cities
city_name=[]
time_inteval=[]        #contains time for runway use

Depart_particular={}
Arrive_particular={}  
Total_particular={}  #Total flights departs and arrives particular city/airport

time_for_schedule={} #required time for individual schedule





with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob3/train1.csv') as csv_file:
    csv_source=csv.reader(csv_file)
    i1=0
    for row in csv_source:
        if(row[6]=='1'):
                i1=i1+1
                Depart.append(row[1])
                Arrive.append(row[2])
                schedule_name.append("schedule1_"+str(i1))
                source_1data[("schedule1_"+str(i1))]=row[0],row[1],row[2],round(int(row[3])/30)

  #  print(schedule_name)
   # print(source_1data[schedule_name[12]])

with open(r'/home/chiraghs/my_codes/python/codestrike_hackhathon/prob3/LatitudeLongitudeCitywise.csv') as csv_file:
    csv_source=csv.reader(csv_file)
    for row in csv_source:
                city_name.append(row[0])
                sla=re.sub("[E|S]",'',row[2])
                for ch in string.punctuation:  #for getting only numbers
                    if((ch!=".") and (ch!="-")):                                                                                                     
                       sla = sla.replace(ch, "")
                slg=re.sub("[E|S]",'',row[3])
                for ch in string.punctuation:
                    if((ch!=".") and (ch!="-")):                                                                                                     
                       slg = slg.replace(ch, "")                
                latlong[row[0]]=sla,slg

    #print(latlong)            

for j in Depart:
    sum=0
    for i in range(len(source_1data)):
        if(j==source_1data[schedule_name[i]][1]):
            #print(source_1data[schedule_name[i]][3])
            sum=sum+source_1data[schedule_name[i]][3]
    Depart_particular[j]=sum

for j in Arrive:
    sum=0
    for i in range(len(source_1data)):
        if(j==source_1data[schedule_name[i]][2]):
            #print(source_1data[schedule_name[i]][3])
            sum=sum+source_1data[schedule_name[i]][3]
    Arrive_particular[j]=sum
    Total_particular[j]=Depart_particular[j]+sum    

#print(Depart_particular)
#print(Arrive_particular)
print(Total_particular)





def timebt(schedule,lat1,long1,lat2,long2):
  slat = radians(float(lat1))
  slon = radians(float(long1))
  elat = radians(float(lat2))
  elon = radians(float(long2))

  dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
  Journey_time = round(dist/800,2)
  #print("The distance is %.2fkm." % dist)
  time_for_schedule[schedule]=Journey_time

#print(source_1data[schedule_name[518]])
#print(latlong[source_1data[schedule_name[518]][1]][0])
#print(latlong[source_1data[schedule_name[518]][1]][1])
#print(latlong[source_1data[schedule_name[518]][2]][0])
#print(latlong[source_1data[schedule_name[518]][2]][1])

for i in range(len(source_1data)):
    timebt(schedule_name[i],latlong[source_1data[schedule_name[i]][1]][0],latlong[source_1data[schedule_name[i]][1]][1]
    ,latlong[source_1data[schedule_name[i]][2]][0],latlong[source_1data[schedule_name[i]][2]][1])

print(time_for_schedule)

sum=0.00      
for i in range(720):
    if(sum==0.6):
        sum=1.00
    time_inteval.append(sum)
    sum=round((sum+0.02),2)      

print(time_inteval) 
print(schedule_name)   