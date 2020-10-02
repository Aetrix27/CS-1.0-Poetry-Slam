import random

filename="poem.txt"

def get_file_lines(filename):
    """This function gets a list of file lines from a text file"""
    infile = open(filename, "r")
    return infile.read().splitlines()

def lines_printed_backwards(lines_list):
    """This function prints a poem backwards, with a line counter in reverse"""
    print("Running lines_printed_backwards\n")
    counter=len(lines_list)
    for line in reversed(lines_list):
        counter-=1
        print(f"{counter} {line}")
    print("\n")

    return

def lines_printed_random(lines_list):
    """This function prints lines in random order from the poem"""
    print("Running lines_printed_random\n")
    for line in lines_list:
        print_line=random.randint(0,len(lines_list)-1)
        print(lines_list[print_line])
    print("\n")

    return

def lines_printed_custom(lines_list):
    """This function prints out every two lines of the poem"""
    line_counter=0
    print("Running lines_printed_custom\n")
    for line in lines_list:
        line_counter+=1
        if (line_counter%2==0):
            print(line)

    return

lines_printed_backwards(get_file_lines(filename))
lines_printed_random(get_file_lines(filename))
lines_printed_custom(get_file_lines(filename))