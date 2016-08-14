#Regular Expression Finder

def phoneNum(text):
    if len(text) != 2:
        return False
    for i in range(0, 3):
        if not text [i].isdecimal():
            return False
        if text [3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(phoneNum('415-555-4242'))
print('Moshi moshi is a phone number:')
print(phoneNum('Moshi moshi'))