#Caesar decipher with key values ranging between 1 and 25 as more than 25 is just repeating
import random

#Taking the input and removing spaces
plaintext = input("Enter your plain text: ").replace(" ","").lower()
print(plaintext)

#Input of the encryption key
key = int(input("Enter the key you want to use: "))%26
while(key==0):
    key = int(input("You Entered multiple of 26 which gives ciphertext same as plaintext, Enter another key: "))%26

#Generating ciphertext(Encryption)
ciphertext = ""
for c in plaintext:
    ciphertext+=chr(((ord(c)+key-97)%26)+97)
print("The ciphertext is :" + ciphertext)

#Brute Forcing all the possible plaintext from ciphertext(Decryption)
for i in range(1,26):
    possibletext = ""
    for c in ciphertext:
        possibletext += chr((((ord(c) - i + 26)%97) % 26) + 97)
    print("Possibility "+ str(i)+" is: " + possibletext)