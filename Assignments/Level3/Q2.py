def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = 'C:/Users/Tejas/Desktop/Consultantadd/Python/Assignments/Level3/doc.txt'
print("Number of lines:", count_lines(file_path))
