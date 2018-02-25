#write the import statements for homework5 functions

from src.homework.homework5 import write_sales_data
from src.homework.homework5 import read_sales_data

def main():
    infile = open('salesrecord.txt', 'w')
    infile.write('name' + '\t' + 'price' + '\n')

    num_of_items = int(input("Enter number of items: "))

    total = 0
    for items in range(1, num_of_items+1):
        item = input('Enter name of item: ')
        price = float(input('Enter price of item: '))

        write_sales_data(infile, item, format(price, '.2f'))
        total += price

    infile.write('total' + '\t'+ str("{0:.2f}".format(total))+ '\n')

    avg = total / num_of_items
    infile.write('Avg' + '\t'+ str("{0:.2f}".format(avg)))
    infile.close()

    file = open('salesrecord.txt', 'r')
    read_sales_data(file)
    file.close()
        
main()
