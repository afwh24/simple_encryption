import os
import sys
from cryptography.fernet import Fernet


#Script current path
path = os.path.dirname(os.path.abspath(sys.argv[0]))

if(path != os.getcwd()): os.chdir(path)



#Generate new encryption key
def generateKey():
    key = Fernet.generate_key()

    with open(path+'/key', 'wb') as keyfile:
        keyfile.write(key)

#Read encryption key
def readKey():
    try:
        with open(path+'/key', "rb") as keyfile:
            key = keyfile.read()

        return Fernet(key)
    
    except Exception as e:
        generateKey();
        print("New keys have been generated due to: ", e, "\n")

#Encryption
def encryption():
    fernet  = readKey()

    for file in os.listdir(path):
        try:
            if file == 'key' or file == 'main.py': continue
            with open(file, 'rb') as original_file:
                original = original_file.read()
            
            encrypted = fernet.encrypt(original)
            with open(file, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
        except Exception as e:
            print(file, " is not encrypted due to ", e, "\n")
            continue

    print("Files have been encrypted\n")


# Decryption
def decryption():
    fernet = readKey()
    for file in os.listdir(path):
        try:
            if file == 'key' or file == 'main.py': continue
            if os.path.isfile(file):
                with open(file, 'rb') as encrypted_file:
                    encrypted = encrypted_file.read()
                
                decrypted = fernet.decrypt(encrypted)

                with open(file, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted)

        except Exception as e:
            print(file, "is not encryptetd due to ", e, "\n")
            continue
        
    print("Files have been decrypted\n")



while True:
    print("=== Menu ===")
    print("1. Generate new encryption key")
    print("2. Encrypt all files")
    print("3. Decrypt all files")
    choice = int(input("Enter your choice: "))

    if choice == 1: generateKey()

    elif choice == 2: encryption()

    elif choice == 3: decryption()

    else:
        print("Program will terminate")
        break

