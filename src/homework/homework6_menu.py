#write import statements for homework 6 functions

import homework6

def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''

    keep_going = 'y'
    
    while keep_going == 'y':
        string1 = input(print('Enter dna string 1 with 10 letters containg A,C,G,T only: '))
        string2 = input(print('Enter dna string 2 with 10 letters containg A,C,G,T only: '))
        print(homework6.get_point_mutations(string1,string2))
        keep_going = input(print('Enter y to try again, anything else to end.'))

                            
def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''

    infile = open('dna_complement.dat', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    infile.close()
    print(homework6.get_dna_complement(line1))
    print(homework6.get_dna_complement(line2))
    print(homework6.get_dna_complement(line3))
    print(homework6.get_dna_complement(line4))

def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''

    infile = open('transcribe_dna_to_rna.dat', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    infile.close()
    print(homework6.transcibe_dna_into_rna(line1))
    print(homework6.transcibe_dna_into_rna(line2))
    print(homework6.transcibe_dna_into_rna(line3))
    print(homework6.transcibe_dna_into_rna(line4))
    print(homework6.transcibe_dna_into_rna(line4))
    print(homework6.transcibe_dna_into_rna(line5))

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''

    infile = open('compute_gc_content.dat', 'r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    infile.close()
    print(homework6.get_gc_content(line1))
    print(homework6.get_gc_content(line2))
    print(homework6.get_gc_content(line3))
    print(homework6.get_gc_content(line4))
    print(homework6.get_gc_content(line5))

def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional

