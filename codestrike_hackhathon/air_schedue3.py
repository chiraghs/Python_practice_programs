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

time_for_journey={} #required time for individual schedule

runway_of_airport={} #runway occupied time for each airport


Final_schedule={}




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
for i in range(len(city_name)):
    runway_of_airport[city_name[i]]=[]




def timebt(schedule,lat1,long1,lat2,long2):
  slat = radians(float(lat1))
  slon = radians(float(long1))
  elat = radians(float(lat2))
  elon = radians(float(long2))

  dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
  Journey_time = round(dist/800,2)
  #print("The distance is %.2fkm." % dist)
  time_for_journey[schedule]=Journey_time

#print(source_1data[schedule_name[518]][1])
#print(latlong[source_1data[schedule_name[518]][1]][0])
#print(latlong[source_1data[schedule_name[518]][1]][1])
#print(latlong[source_1data[schedule_name[518]][2]][0])
#print(latlong[source_1data[schedule_name[518]][2]][1])

for i in range(len(source_1data)):
    timebt(schedule_name[i],latlong[source_1data[schedule_name[i]][1]][0],latlong[source_1data[schedule_name[i]][1]][1]
    ,latlong[source_1data[schedule_name[i]][2]][0],latlong[source_1data[schedule_name[i]][2]][1])

#print(time_for_journey)
depart_time=0.00

def Check(depart_time):
 try:
    if(depart_time<0.6):
      depart_time=depart_time+0.02
      return depart_time
    if(depart_time>=0.6 and depart_time<=1.00):
        depart_time=1.00 

    if(depart_time>=1.00 and depart_time<1.6):
      depart_time=depart_time+0.02
      return depart_time
    if(depart_time>=1.6 and depart_time<=2.00):
      depart_time=2.00


    if(depart_time>=2.00 and depart_time<2.6):
      depart_time=depart_time+0.02
      return depart_time
    if(depart_time>=2.6 and depart_time<=3.00):
      depart_time=3.00 
      return depart_time

    if(depart_time>3.00 and depart_time<3.6):
      depart_time=depart_time+0.02
      return depart_time
    if(depart_time>=3.6 and depart_time<=4.00):
      depart_time=4.00 
      return depart_time      

    if(depart_time>=4.00 and depart_time<4.6):
      depart_time=depart_time+0.02
      return depart_time
    if(depart_time>=4.6 and depart_time<=5.00):
      depart_time=5.00 
      return depart_time

 except:RecursionError
 #print(runway_of_airport)               

def Schedule(depart_time,schedule_name,jtime):
    if((depart_time not in runway_of_airport[source_1data[schedule_name][1]]) and ((depart_time+jtime) not in runway_of_airport[source_1data[schedule_name][2]])):
        Final_schedule[schedule_name]=schedule_name,source_1data[schedule_name][0],source_1data[schedule_name][1],source_1data[schedule_name][2],depart_time,depart_time+jtime
        runway_of_airport[source_1data[schedule_name][1]].append(depart_time)
        runway_of_airport[source_1data[schedule_name][2]].append(depart_time+jtime)
        with open('/home/chiraghs/my_codes/python/codestrike_hackhathon/prob3/solution.csv',mode='a+') as csv_file:
            fieldnames=['Airline','Departing_Port','Arriving_Port','Departure_Time','Arrival_Time']

            writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
            writer.writeheader()
            #print(Final_schedule)
            for v in range(len(Final_schedule)):
               writer.writerow({'Airline': Final_schedule[schedule_name][1],'Departing_Port': Final_schedule[schedule_name][2],'Arriving_Port':Final_schedule[schedule_name][3],'Departure_Time': Final_schedule[schedule_name][4],'Arrival_Time':Final_schedule[schedule_name][5]})
    else:
        Schedule(Check(depart_time),schedule_name,jtime)   

for i in range(len(source_1data)):
    Schedule(depart_time,schedule_name[i],time_for_journey[schedule_name[i]])

#print(source_1data[schedule_name[0]][2])    
#print(runway_of_airport)
#print(Final_schedule)