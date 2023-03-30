def validate_input(word):
    if len(word) == 0:
        return False
    if word[0] != 'a':
        return False
    i = 1
    while i < len(word) and word[i] == 'a':
        i += 1
    if i == len(word):
        return False
    if word[i] != 'b':
        return False
    i += 1
    while i < len(word) and word[i] == 'b':
        i += 1
    return i == len(word)

while True:
    word = input("Enter a word to validate (or 'quit' to exit): ")
    if word == 'quit':
        break
    if validate_input(word):
        print("Valid input!")
    else:
        print("Invalid input!")
