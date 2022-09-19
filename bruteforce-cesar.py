import time
letters = "abcdefghijklmnopqrstuvwxyz"
print("Please enter your encoded string > ")
encoded_string = input()
start_time = time.time()
x = 0
while x < 26:
    x = x + 1
    string_to_decrypt = encoded_string.lower()
    cipher_shift = int(x)
    string_decrypted = ""
    for character in string_to_decrypt:
        position = letters.find(character)
        new_position = position - cipher_shift
        if character in letters:
            string_decrypted = string_decrypted + letters[new_position]
        else:
            string_decrypted = string_decrypted + character
    print("Cipher shift > "+ str(cipher_shift))
    print("Message      > "+ str(string_decrypted))
print("--- %s seconds ---" % (time.time() - start_time))
