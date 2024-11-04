import os
import pyaes


file_name = "teste.txt"
# Chave de criptografia (16 bytes para AES-128)
key = b'1234567890123456'

# Criptografar o arquivo
with open(file_name, 'rb') as file:
    file_data = file.read()
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypt_data = aes.encrypt(file_data)


# Salvar o arquivo criptografado
encrypted_file_name = "teste.txt.enc"
with open(encrypted_file_name, 'wb') as encrypted_file:
    encrypted_file.write(encrypt_data)

print(f"Arquivo '{file_name}' criptografado como '{encrypted_file_name}'.")


os.remove(file_name)