filename="poem.txt"

infile = open(filename, "r")

def get_file_lines(filename):

    for line in infile:
        return infile.readlines()

print(get_file_lines(filename))