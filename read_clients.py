def main():

    infile = open('clients.txt', 'r')
    number = 0

    for i in infile:
        number = number + 1
        i = i.rstrip('\n')
        print(number, '. ' + i, sep='')
        
    infile.close()

main()