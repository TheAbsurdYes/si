from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_ECB
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# noduri ={
#     'A' : [],
#     'B' : [],
#     'KM' : {
#         'K': '',
#         "K'" : get_random_bytes(16)
#     }
# }

# noduri['A'].append('ECB')
# noduri['B'].append('ECB')

# print(noduri['A'])

# noduri['KM']['K'] = get_random_bytes(16)

# print(noduri['KM']['K'])

# cipher = AES.new(noduri['KM']["K'"],AES.MODE_ECB)

# noduri['KM']['K'] = cipher.encrypt(b'Salut')

data = b'salut'

# for i in data:
#     print(i)

# key = get_random_bytes(16)
# cipher = AES.new(key,MODE_ECB)
# ciphertext = cipher.encrypt(pad(data,AES.block_size))

# print(ciphertext)

# plaintext = unpad(cipher.decrypt(ciphertext),AES.block_size)

# print(plaintext)
