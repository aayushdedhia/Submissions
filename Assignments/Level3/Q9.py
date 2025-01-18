def run_length_encoding(string):
    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1] + str(count)
            count = 1
    result += string[-1] + str(count)

    return result

input_string = input("Enter String: ")
encoded = run_length_encoding(input_string)
print(f"Encoded string: {encoded}")
