import pyaes

encrypted_file_name = "teste.txt.enc"

key = b'1234567890123456'

# Ler o conteúdo do arquivo criptografado
with open(encrypted_file_name, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Criar uma nova instância AES para descriptografar
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(encrypted_data)

# Salvar o conteúdo descriptografado em um novo arquivo
decrypted_file_name = "teste_decrypted.txt"
with open(decrypted_file_name, 'wb') as decrypted_file:
    decrypted_file.write(decrypt_data)

print(f"Arquivo '{encrypted_file_name}' foi descriptografado como '{decrypted_file_name}'.")
