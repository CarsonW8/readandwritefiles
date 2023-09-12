import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers) #can add ,delimiter=' '. whatever seperates the file

outfile = open('customer_country.csv', 'w')

next(csv_file) #skips a row

x = 0

outfile.write("Full name,Country\n")

for rec in csv_file:
    #print(rec)
    outfile.write(f"{rec[1]} ")
    outfile.write(f"{rec[2]},")
    outfile.write(f"{rec[4]}\n")
    x+=1

outfile.write(f"Total number of customers: ")
outfile.write(str(x))

outfile.close()
