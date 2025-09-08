alphabet = "abcdefghijklmnopqrstuvwxyz"
key_length = int(input("Please enter length of key: "))
letter = input("Please enter your letter: ").lower()
encrypted_letter=""
for i in letter:
    if i in alphabet:
        position = (key_length + alphabet.index(i)) % 26
        encrypted_char=alphabet[position]
        encrypted_letter=encrypted_char+encrypted_letter 
       
    else:
        encrypted_letter=encrypted_letter+ i
print(f"Encrypted letter: {encrypted_letter}")