import csv

with open(r'/home/chiraghs/Downloads/crowdstrike/Airlines Data CrowdStrike - RawTest_v5.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    for row in csv_reader:
        print(row)