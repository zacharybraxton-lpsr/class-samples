# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
# 
# Author: mflax [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
import string
def createDictionary(key):
  alphacode = list(string.ascii_lowercase)
  Alphacode = list(string.ascii_uppercase)
  setUp = {}
  count = 0
  for a in alphacode:
    setUp[a] = alphacode[(count + key) % 26]
    count += 1
  for A in Alphacode:
    setUp[A] = Alphacode[(count + key) % 26]
    count += 1
    setUp[" "] = " "
  return setUp
  




# gets the encrypted message from the user
# arguments: none
# returns: encoded message
def getMessage(message):
	return message

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
  newStr = ''
  for m in message:
    newMsg = dictionary[m]
    newStr = newStr + newMsg
  return newStr
    
  
    
# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(decMessage):
	print(decMessage)


# execution starts here

# ask user for key
print("What key would you like to use to decode? If you want to encode, just choose a number lower than 26 and subtract it from 26")
try:
  key = int(raw_input())
except:
  print("Sorry, we cannot create a dictionary based on this code, try again!")
dictionary = createDictionary(key)
print('What is the message you would like to decode/encode?')
blip = raw_input()

try:
  encodedMessage = getMessage(blip)
  decodedMessage = decodeMessage(encodedMessage, dictionary)
  print("Here is your decoded/encoded message!")
  print("")
  printMessage(decodedMessage)
except:
  print("Sorry, the message or key you entered can not be processed, try again.")
