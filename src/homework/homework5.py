#Create a function named write_sales_data with file_object, item and price as parameters.
#The function should write item and price to a file.

#Create another function named read_sales_data with file_object as a parameter.
#The function will read the file line by line and display to screen to produce the table described in homework 5.

def write_sales_data(item,price):
    outfile = open('file_object.txt','a')
    outfile.write(item)
    outfile.write(" ")
    outfile.write(str(price))
    outfile.write('\n')
    outfile.close()

def read_sales_data():
    infile = open('file_object.txt', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    line6 = infile.readline()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    
    infile.close()

