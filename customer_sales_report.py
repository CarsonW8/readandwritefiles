import csv

custid = '250'
total = 0

salesdata = open('sales.csv', 'r')
outfile = open('salesreport.csv', 'w')

csv_file = csv.reader(salesdata)
next(csv_file)

outfile.write("Customer ID, Total\n")

for rec in csv_file:
    if custid == rec[0]:
        total += rec [3] + rec[4] + rec[5]
    else:
        outfile.write(custid, total)
        #write custid and total to the outfile
        #250, 200 (if 200 is total)
        custid = rec[0] #assign custid to the next one (251)
        total = rec[3] + rec[4] + rec[5]
#write the custid and total to the outfile for the last record (261)
