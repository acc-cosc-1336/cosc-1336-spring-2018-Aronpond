from src.homework.homework8 import add_inventory, remove_inventory_widget
'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''


def main():
    contin = 'y'
    widgets = {}
    while contin == 'y':
        widget_name = input('Type the item you wish to add: ')
        quantity = int(input('How many do you wish to add: '))
        add_inventory(widgets,widget_name,quantity)
        contin = input('Enter y to continue, enter anything else to finish. ')

    
    if contin != 'y':
        outfile = open('Inventory.txt', 'w')
        for i in widgets:
            outfile.write(i)
            outfile.write(' ')
            outfile.write(str(widgets[i]))
            outfile.write('\n')
        outfile.close()
        return

main()
