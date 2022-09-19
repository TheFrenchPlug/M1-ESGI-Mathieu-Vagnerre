import time
letters = "abcdefghijklmnopqrstuvwxyz"
print("Please enter your string > ")
string_to_encode = input()
print("Please enter your shift > ")
cipher_shift = input()
string_to_encode = string_to_encode.lower()
cipher_shift = int(cipher_shift)
string_encrypted = ""
start_time = time.time()
for character in string_to_encode:
    position = letters.find(character)
    new_position = (position + cipher_shift) % 26
    if character in letters:
        string_encrypted = string_encrypted + letters[new_position]
    else:
        string_encrypted = string_encrypted + character
print("Cipher shift > "+ str(cipher_shift))
print("Message      > "+ str(string_encrypted))
print("--- %s seconds ---" % (time.time() - start_time))