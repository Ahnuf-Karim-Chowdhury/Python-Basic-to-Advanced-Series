# This Password Manager uses - 
# AES-256 for symmetric-key and 
# RSA-4096 for public-key encryption to secure the password and the usernames

#First it takes the Plain text then encrypts it using AES-256 
#after that it encrypts the AES-256 data using RSA-4096 .

#In Conclusion, it is a double encryption Password Manager.
#Multiple Accounts can be created using a Master Password for each Account.
#Each and every account can have multiple platforms(usernames & passwords) saved within them.

import json
import base64
import os
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# File to store encrypted data
ENCRYPTED_FILE = 'pass_key.txt'

# Generate RSA key pair
def generate_rsa_keys():
    key = RSA.generate(4096)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Load or generate RSA keys
def load_rsa_keys():
    if os.path.exists('private_key.pem') and os.path.exists('public_key.pem'):
        with open('private_key.pem', 'rb') as f:
            private_key = f.read()
        with open('public_key.pem', 'rb') as f:
            public_key = f.read()
    else:
        private_key, public_key = generate_rsa_keys()
        with open('private_key.pem', 'wb') as f:
            f.write(private_key)
        with open('public_key.pem', 'wb') as f:
            f.write(public_key)
    return private_key, public_key

# Encrypt data with AES
def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Decrypt data with AES
def decrypt_aes(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

# Encrypt data with RSA
def encrypt_rsa(data, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    enc_data = cipher_rsa.encrypt(data)
    return base64.b64encode(enc_data).decode('utf-8')

# Decrypt data with RSA
def decrypt_rsa(enc_data, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    enc_data = base64.b64decode(enc_data)
    data = cipher_rsa.decrypt(enc_data)
    return data

# Create account
def create_account():
    master_password = getpass("Enter a master password: ")
    confirm_password = getpass("Confirm the master password: ")
    if master_password != confirm_password:
        print("Passwords do not match.")
        return
    
    # AES key for encrypting the data
    aes_key = get_random_bytes(32)
    iv, enc_password = encrypt_aes(master_password, aes_key)

    private_key, public_key = load_rsa_keys()
    enc_aes_key = encrypt_rsa(aes_key, public_key)

    account_data = {
        'aes_key': enc_aes_key,
        'iv': iv,
        'password': enc_password
    }

    with open(ENCRYPTED_FILE, 'w') as f:
        json.dump(account_data, f)
    print("Account created successfully.")

# Login account
def login_account():
    master_password = getpass("Enter your master password: ")

    with open(ENCRYPTED_FILE, 'r') as f:
        account_data = json.load(f)

    private_key, _ = load_rsa_keys()
    aes_key = decrypt_rsa(account_data['aes_key'], private_key)
    iv = account_data['iv']
    decrypted_password = decrypt_aes(iv, account_data['password'], aes_key)

    if master_password == decrypted_password:
        print("Login successful.")
        return aes_key
    else:
        print("Invalid master password.")
        return None

# Show platform data
def show_platform_data(aes_key):
    with open(ENCRYPTED_FILE, 'r') as f:
        account_data = json.load(f)
    
    iv = account_data['iv']
    encrypted_data = account_data.get('platform_data', {})
    print("---------------------------------------------")
    for platform, data in encrypted_data.items():
        username, password = decrypt_aes(data['iv'], data['password'], aes_key).split(':')
        print(f"Platform: {platform}\nUsername: {username}\nPassword: {password}\n")
    print("---------------------------------------------")

# Entry platform data
def entry_platform_data(aes_key):
    platform = input("Enter platform name: ")
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    iv, enc_password = encrypt_aes(f"{username}:{password}", aes_key)
    with open(ENCRYPTED_FILE, 'r') as f:
        account_data = json.load(f)

    if 'platform_data' not in account_data:
        account_data['platform_data'] = {}

    account_data['platform_data'][platform] = {
        'iv': iv,
        'password': enc_password
    }

    with open(ENCRYPTED_FILE, 'w') as f:
        json.dump(account_data, f)

    print("Platform data added successfully.")

# Delete platform data
def delete_platform_data(aes_key):
    platform = input("Enter platform name to delete: ")
    with open(ENCRYPTED_FILE, 'r') as f:
        account_data = json.load(f)

    if 'platform_data' in account_data and platform in account_data['platform_data']:
        del account_data['platform_data'][platform]
        with open(ENCRYPTED_FILE, 'w') as f:
            json.dump(account_data, f)
        print("Platform data deleted successfully.")
    else:
        print("Platform data not found.")

# Edit platform data
def edit_platform_data(aes_key):
    platform = input("Enter platform name to edit: ")
    with open(ENCRYPTED_FILE, 'r') as f:
        account_data = json.load(f)

    if 'platform_data' in account_data and platform in account_data['platform_data']:
        new_username = input("Enter new username (leave blank to keep current): ")
        new_password = getpass("Enter new password (leave blank to keep current): ")

        current_data = account_data['platform_data'][platform]
        current_username, current_password = decrypt_aes(current_data['iv'], current_data['password'], aes_key).split(':')

        if new_username:
            current_username = new_username
        if new_password:
            current_password = new_password

        iv, enc_password = encrypt_aes(f"{current_username}:{current_password}", aes_key)
        account_data['platform_data'][platform] = {
            'iv': iv,
            'password': enc_password
        }

        with open(ENCRYPTED_FILE, 'w') as f:
            json.dump(account_data, f)
        print("Platform data updated successfully.")
    else:
        print("Platform data not found.")

# Main function
def main():
    while True:
        print("\n1. Create Account")
        print("2. Login Account")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            aes_key = login_account()
            if aes_key:
                while True:
                    print("\n1. Show Platform Data")
                    print("2. Entry Platform Data")
                    print("3. Delete Platform Data")
                    print("4. Edit Platform Data")
                    print("5. Logout")
                    choice = input("Choose an option: ")

                    if choice == '1':
                        show_platform_data(aes_key)
                    elif choice == '2':
                        entry_platform_data(aes_key)
                    elif choice == '3':
                        delete_platform_data(aes_key)
                    elif choice == '4':
                        edit_platform_data(aes_key)
                    elif choice == '5':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            break
        else:
            print("Invalid option.")

main()
