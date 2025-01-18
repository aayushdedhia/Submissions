def even_length_strings(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        words = content.split()
        even_length_words = [word for word in words if len(word) % 2 == 0]
        return " ".join(even_length_words)


file_path = 'C:/Users/Tejas/Desktop/Consultantadd/Python/Assignments/Level3/doc.txt' 
print(even_length_strings(file_path))
