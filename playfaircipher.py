#playfaircipher with matrix formation filled with key first and remaining alphabets next
import numpy as np

#creating matrix of dimensions 5x5 using the key
alphabets = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = input("Enter the playfair key: " ).lower().replace(" ","")
matrix = np.chararray((5,5),unicode=True)
unique = {}
col=0
row=0
for i in key:
    if i not in unique:
        alphabets.remove(i)
        matrix[row][col]=i
        if(col==4):
            row+=1
        col=(col+1)%5
for i in alphabets:
    matrix[row][col] = i
    if (col == 4):
        row += 1
    col = (col + 1) % 5
print(matrix)

#Encrypting the input text using the matrix
plaintext = input("Enter your plain text: ").replace(" ","").lower()
intlen = len(plaintext)
if(intlen%2==1):
    plaintext+='z'
#splitting the input text into bigrams
bigrams = []
i=0
while i<intlen:
    #print("value of i: "+str(i))
    if(plaintext[i]==plaintext[i+1]):
        bigrams.append(plaintext[i]+'x')
        i+=1
    elif(plaintext[i]=='j'):
        bigrams.append('i'+plaintext[i+1])
        i=i+2
    elif(plaintext[i+1]==""):
        bigrams.append(i+'z')
    else:
        bigrams.append(plaintext[i]+plaintext[i+1])
        #print('its here')
        i=i+2

print(bigrams)

#encrypting using the bigrams formed

def matrix_find(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j]==str(value)):
                return [i,j]

print(str(matrix[0][0]))

[row1,col1] = matrix_find(matrix,'m')
print(row1)
print(col1)

encryptedtext = ""
for i in bigrams:
    #print(i[0])
    #print(i[1])
    row1,col1 = matrix_find(matrix,i[0])
    row2,col2 = matrix_find(matrix,i[1])
    if row1==row2:
        encryptedtext+=matrix[row1][(col1+1)%5]+matrix[row2][(col2+1)%5]
    elif col1==col2:
        encryptedtext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
    else:
        encryptedtext+= matrix[row1][col2] + matrix[row2][col1]

print("The encrpyted text is: " + encryptedtext)

#Decryption when Decrypted text is given and key is known
ciphertext = input("Enter your plain text: ").replace(" ","").lower()
digrams = []
i=0
while i<len(ciphertext):
    #print("value of i: "+str(i))
    if(ciphertext[i]==ciphertext[i+1]):
        digrams.append(ciphertext[i]+'x')
        i+=1
    elif(ciphertext[i]=='j'):
        digrams.append('i'+ciphertext[i+1])
        i=i+2
    else:
        digrams.append(ciphertext[i]+ciphertext[i+1])
        #print('its here')
        i=i+2
print(digrams)

#Decrypting using the key matrix we already have
decryptedtext = ""
for i in digrams:
    #print(i[0])
    #print(i[1])
    row1,col1 = matrix_find(matrix,i[0])
    row2,col2 = matrix_find(matrix,i[1])
    if row1==row2:
        decryptedtext+=matrix[row1][(col1-1)%5]+matrix[row2][(col2-1)%5]
    elif col1==col2:
        decryptedtext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
    else:
        decryptedtext+= matrix[row1][col2] + matrix[row2][col1]

print("The encrpyted text is: " + decryptedtext)







