def validate_input(word):
    stack = []
    for char in word:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0

def validate_word(word):
    if len(word) == 0:
        return False
    elif word == "()":
        return True
    elif word[0] == "(" and word[-1] == ")":
        return validate_input(word[1:-1])
    else:
        return False

while True:
    word = input("Enter a word to validate (or 'quit' to exit): ")
    if word == 'quit':
        break
    if validate_word(word):
        print("Valid input!")
    else:
        print("Invalid input!")
