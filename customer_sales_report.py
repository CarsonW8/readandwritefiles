import csv

custid = '250'
total = 0

salesdata = open('sales.csv', 'r')
outfile = open('salesreport.csv', 'w')

csv_file = csv.reader(salesdata)
next(csv_file)

outfile.write("Customer ID,Total\n")

for rec in csv_file:
    if custid == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
        #add recs3,4,5
    else:
        outfile.write(custid)
        outfile.write(',')
        outfile.write(f"{total:.2f}\n")
        custid = rec[0] #assign custid to the next one (251)
        total = float(rec[3]) + float(rec[4]) + float(rec[5])

outfile.write(custid)
outfile.write(',')
outfile.write(f"{total:.2f}\n")

outfile.close()
