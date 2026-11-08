
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code
    characters_code = ord(char)

    # add one to the character's code
    new_characters_code = characters_code + 1

    # convert the code back to a character
    new_char = chr(new_characters_code)

    # add encrypted character to encrypted text
    encrypted_text = encrypted_text+ new_char

print(plain_text)
print(encrypted_text)