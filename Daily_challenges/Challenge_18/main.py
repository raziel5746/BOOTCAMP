alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

action = int(input("Type '1' to cypher.\nType '2' to decypher: "))

def execute():
    if action == 1:
        encrypt()
    elif action == 2:
        decrypt()

def encrypt():
    encrypted = ""
    msg_to_encrypt = input("Enter a message to encrypt: ")
    shift = int(input("Enter an integer to set the shift: "))
    for i in range(len(msg_to_encrypt)):
        encrypted += alphabet[(alphabet.index(msg_to_encrypt[i]) + shift) % len(alphabet)]
    print(encrypted)

def decrypt():
    decrypted = ""
    msg_to_decrypt = input("Enter a message to decrypt: ")
    shift = int(input("Enter an integer to set the shift: "))
    for i in range(len(msg_to_decrypt)):
        decrypted += alphabet[(alphabet.index(msg_to_decrypt[i]) - shift) % len(alphabet)]
    print(decrypted)

execute()


##==================================================================
## Another way of doing it, but it doesn't accept a huge value for the shift, and it doesn't use just letters for encrypting

# array_cypher = []
# array_decypher = []

# def execute():

#     action = input("Type '1' to cypher. Type '2' to decypher: ")
#     if action == "1":
#         cypher()
#     if action == "2":
#         decypher()

# def cypher():
#     X = int(input("Enter an integer to set the shift: "))
#     text_to_cypher = input("Enter text to cypher: ")
#     for i in range(len(text_to_cypher)):
#         if text_to_cypher[i] == " ":
#             array_cypher.append(" ")
#         else:
#             array_cypher.append(chr(ord(text_to_cypher[i]) - X))
#     cyphered = "".join(array_cypher)
#     print("Chyphered text: " + cyphered)

# def decypher():
#     text_to_decypher = input("Enter text to decypher: ")
#     for i in range(len(text_to_decypher)):
#         if text_to_decypher[i] == " ":
#             array_decypher.append(" ")
#         else:
#             array_decypher.append(chr(ord(text_to_decypher[i]) + X))
#     decyphered = "".join(array_decypher)
#     print("Decyphered text: " + decyphered)

# execute()



