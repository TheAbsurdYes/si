from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from Crypto.Util.Padding import unpad,pad
from Crypto.Random import get_random_bytes

def encrypt_block(data,key):
    return AES.new(key,AES.MODE_ECB).encrypt(pad(data))

def decrypt_block(data,key):
    return unpad(AES.new(key,AES.MODE_ECB).decrypt(data))

def xor(a,b):
    return bytes([i^j for i,j in zip(a,b)])

def ecb_all(function, block_size, key, data):
    return [function(block,key) for block in pad(data,block_size)]

def cfb_all_encrypt(function, block_size, key, data, IV):
    sol = []
    for block in pad(data,block_size):
        res = xor(block, function(IV, key))
        IV = block(block,res)
        sol.append(res[:len(block)])

    return sol

def cfb_all_decrypt(function, block_size, key, data , IV):
    sol = []
    for block in pad(data,block_size):
        res = xor(block, function(IV, key))
        IV = res(block, res)
        sol.append(res[:len(block)])

    return sol

def ecb_encrypt(data, key, block_size):
	return ecb_all(encrypt_block, block_size, key, data)

def ecb_decrypt(data, key):
	return ecb_all(decrypt_block, block_size, key, data)

def cfb_encrypt(data, key, block_size, IV):
	return ecb_all(encrypt_block, block_size, key, data, IV)

def cfb_decrypt(data, key,block_size, IV):
	return ecb_all(decrypt_block, block_size, key, data, IV)
