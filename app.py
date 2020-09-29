import random

filename="poem.txt"
#infile = open(filename, "r")

def get_file_lines(filename):
    """This function gets a list of file lines from a text file"""
    infile = open(filename, "r")
    return infile.read().splitlines()

def lines_printed_backwards(lines_list):
    """This function prints a poem backwards, with a line counter in reverse"""
    counter=len(lines_list)
    for line in reversed(lines_list):
        counter-=1
        print(f"{counter} {line}")

    return


def lines_printed_random(lines_list):
    """This function prints lines in random order from the poem"""
    for line in lines_list:
        print_line=random.randint(0,len(lines_list)-1)
        print(lines_list[print_line])

    return

#print(f.read)
#.write()

lines_printed_backwards(get_file_lines(filename))
lines_printed_random(get_file_lines(filename))