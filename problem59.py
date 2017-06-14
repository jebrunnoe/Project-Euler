from collections import	Counter

cipher = open("p059_cipher.txt", "r").read().split(',')
cipher_length = len(cipher)
key_length = 3

def sort(cipher):
   groups = list()
   for group in range(key_length): groups.append([])
   for i in range(cipher_length):
      groups[i % 3].append(cipher[i])
   return groups

def analyze(groups):
   modes = list()
   for group in range(key_length):
      modes.append(Counter(groups[group]).most_common(1)[0][0])
   key = list()
   for k in range(key_length):
      key.append(int(modes[k]) ^ ord(" "))
   return key

def decrypt(cipher, key):
   message = list()
   for i in range(cipher_length):
      message.append(chr(int(cipher[i]) ^ key[i % 3]))
   return "".join(message)

groups = sort(cipher)
key = analyze(groups)
message = decrypt(cipher, key)
print message
print sum([ord(i) for i in message])
