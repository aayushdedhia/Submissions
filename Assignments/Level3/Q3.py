def JtoI(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        corrected_content = content.replace('J', 'I')
        print(corrected_content)

file_path = 'C:/Users/Tejas/Desktop/Consultantadd/Python/Assignments/Level3/words.txt'
JtoI(file_path)
