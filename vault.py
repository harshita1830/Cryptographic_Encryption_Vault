from cryptography.fernet import Fernet
import os

# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encrypt files
def encrypt_folder(folder_path, fernet):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                data = file.read()

            encrypted = fernet.encrypt(data)

            with open(file_path, "wb") as file:
                file.write(encrypted)

            print(f"{filename} encrypted.")

# Decrypt files
def decrypt_folder(folder_path, fernet):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                data = file.read()

            decrypted = fernet.decrypt(data)

            with open(file_path, "wb") as file:
                file.write(decrypted)

            print(f"{filename} decrypted.")

# Main Program
generate_key()
key = load_key()
fernet = Fernet(key)

folder = "test_folder"

print("Encrypting files...")
encrypt_folder(folder, fernet)

print("Decrypting files...")
decrypt_folder(folder, fernet)

print("Process completed successfully!")