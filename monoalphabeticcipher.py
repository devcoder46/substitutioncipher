#monoaplhabetic cipher with 26! permutations possible keys where each alphabet gets unique alphabet
import random
import operator

#alphabets string
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
orgmap = "abcdefghijklmnopqrstuvwxyz"

#Taking key as input
key = input("Enter the key you want to use: ").replace(" ","").lower()
unique = sorted(set(key),key=key.index)
encryptkey = ""
for i in unique:
    encryptkey+=i
    alphabets.remove(i)

for i in alphabets:
    encryptkey+=i

print(encryptkey)

#now encryption using encryptkey
plaintext = input("Enter your plain text: ").replace(" ","").lower()
print(plaintext)
ciphertext = ""
for i in plaintext:
    ciphertext += encryptkey[orgmap.find(i)]

print(ciphertext)

#Decryption using frequency table for english language(single letter occurence works well for large encrypted data)
order = "eariotnslcudpmhgbfywkvxzjq"
freq = ""
codedtext = input("Enter your encoded text: ").replace(" ","").lower()
occurences = {}
for i in codedtext:
    if i in occurences:
        occurences[i]+=1
    else:
        occurences[i]=1

decsort = sorted(occurences.items(),key=operator.itemgetter(1),reverse=True)
for key,value in decsort:
    freq+=key

print(freq)

encryptedcode = ""
for i in codedtext:
    encryptedcode+= order[freq.find(i)]

print("The plaintext is: " + encryptedcode)

#Decyption using bigrams as frequency table
order2 = ['th','he','in','er','an','re','nd','at','on','nt','ha','es','st','en','ed','to','it','ou','ea','hi',
          'is','or','ti','as','te','et','ng','of','al','de','se','le','sa','si','ar','ve','ra','ld','ur']
occurences2 = {}
bimap = {}
for i in range(len(codedtext)-1):
    if (codedtext[i]+codedtext[i+1]) in occurences2:
        occurences2[codedtext[i]+codedtext[i+1]]+=1
    else:
        occurences2[codedtext[i]+codedtext[i+1]]=1
print(occurences2)

decsort2 = sorted(occurences2.items(),key=operator.itemgetter(1),reverse=True)
print(decsort2)
cnt = 0
for key in decsort2:
    if (key[0][0] not in bimap and key[0][1] not in bimap):
        bimap[key[0][0]] = order2[cnt][0]
        bimap[key[0][1]] = order2[cnt][1]
    if(cnt<len(order2)-1):
        cnt+=1
    else:
        break

print(bimap)

for i in encryptedcode:
    if i in bimap:
        print(bimap[i])
        encryptedcode = encryptedcode.replace(i,bimap[i])

print(encryptedcode)
