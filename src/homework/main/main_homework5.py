#write the import statements for homework5 functions
from homework5 import write_sales_data
from homework5 import read_sales_data
#With the functions created in homework5...
#Prompt user for number of sales records to input.
n = int(input(print('How many sales need inputing?')))
#Open a file for text writing.
outfile = open('file_object.txt','w')              
#Iterate and prompt user for item name and price.
item1 = input(print('enter item 1'))
price1 = float(input(print('enter price for item 1')))
item2 = input(print('enter item 2'))
price2 = float(input(print('enter price for item 2')))
item3 = input(print('enter item 3'))
price3 = float(input(print('enter price for item 3')))
item4 = input(print('enter item 4'))
price4 = float(input(print('enter price for item 4')))
#Save item name and price to file in one line
write_sales_data(item1,price1)
write_sales_data(item2,price2)
write_sales_data(item3,price3)
write_sales_data(item4,price4)
#Calculate sum of price and write to file
outfile = open('file_object.txt','a')
total = float(price1) + float(price2) + float(price3) + float(price4)
outfile.write('total ')
outfile.write(str(format(total, '.2f')))
outfile.write('\n')
outfile.close()
#Calculate average price and write to file
average = total / 4
outfile = open('file_object.txt','a')
outfile.write('average price ')
outfile.write(str(format(average, '.2f')))
outfile.close()
#Open a file for text reading.
read_sales_data()
#Read the saved file and output table

