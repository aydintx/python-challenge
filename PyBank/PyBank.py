import os 
import csv
file = "budget_data.csv"

with open(file, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
csvpath = os.path.join(file)

with open(csvpath, newline='') as csvfile:



#   CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')



#     print(csvreader)

#    Read the header row first (skip this step if there is now header)

    csv_header = next(csvreader)

    #print(f"CSV Header: {csv_header}")



    # Read each row of data after the header
    months=0
    total=0
    ave_change=0
    gre_inc=0
    gre_dec=0

    panl=[]
    all_csv=[]

    for row in csvreader:

        #print(row)
        months+=1

        total+=int(row[1])

        panl.append(int(row[1]))

        all_csv.append([row[0], int(row[1])])

#     print(panl)
sum=0

changes=[]

length=len(panl)-1

#loop through panl list to get the average, max inc and dec

for i in range(0,length):

        changes.append(panl[i+1]- panl[i])

        sum = sum + changes[i]



#print(f" this is the changes changes{changes}") 

ave_change=sum/(i+1) 

gre_inc=max(changes)

gre_inc_ind=changes.index(max(changes))+1 #gre_inc_ind

gre_dec=min(changes)

gre_dec_ind=changes.index(min(changes))+1 #gre_dec_ind
print(f"Financial Analysis")

print(f"----------------------------------------")

print(f"Total months: {months}")

print(f"Total: ${total}")

print(f"Average  Change: ${round(ave_change, 2)}")

print(f"Greatest Increase: {all_csv[gre_inc_ind][0]}, ${gre_inc}")

print(f"Greatest Decrease: {all_csv[gre_dec_ind][0]}, ${gre_dec}")
