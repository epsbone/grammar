# Define grammar rules as functions
def S(word):
    return A(word) or C(word)

def A(word):
    if word.startswith('a'):
        return B(word[1:])
    elif word.startswith('ab'):
        return B(word[2:])
    else:
        return False

def B(word):
    if word.startswith('cd'):
        return True
    elif word.startswith('c') and B(word[1:]) and word.endswith('d'):
        return True
    else:
        return False

def C(word):
    if word.startswith('a'):
        return D(word[1:])
    elif word.startswith('a') and C(word[1:]) and word.endswith('d'):
        return True
    else:
        return False

def D(word):
    if word.startswith('bc'):
        return True
    elif word.startswith('b') and D(word[1:]) and word.endswith('c'):
        return True
    else:
        return False


# Use the grammar rules to validate input
def validate_word(word):
    return S(word)


# Test the input validation
while True:
    word = input("Enter a word to validate (or 'quit' to exit): ")
    if word == 'quit':
        break
    if validate_word(word):
        print("Valid input!")
    else:
        print("Invalid input!")
