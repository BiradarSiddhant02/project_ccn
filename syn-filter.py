file_path = '/home/siddhant/Documents/project_ccn/cap.txt'

with open(file_path, 'r') as file:
    new_lines = [line for line in file if line.rstrip().endswith('A')]

# Now new_lines contains the lines that end with 'S'
for i in new_lines:
    print(i)
