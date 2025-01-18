def parse_encoded_string(encoded_string):
    parts = encoded_string.split("0")
    parts = [p for p in parts if p]
    return {"first_name": parts[0], "last_name": parts[1], "id": parts[2]}

encoded = input("Enter string: ")
parsed = parse_encoded_string(encoded)
print(parsed)
