filename="poem.txt"
infile = open(filename, "r")

def get_file_lines(filename):
    """This function gets a list of file lines from a text file"""
    for line in infile:
        #split_line_list= line.rstrip().split("\n")
        return infile.readlines()

#print(get_file_lines(filename))

def lines_printed_backwards(lines_list):
    counter=len(lines_list)
    for line in reversed(lines_list):
        counter-=1
        print(f"{counter} {line}")

    return
    #return list(reversed(lines_list))
    #return line.rstrip()

#print(f.read)
#.write()

lines_printed_backwards(get_file_lines(filename))

infile.close()