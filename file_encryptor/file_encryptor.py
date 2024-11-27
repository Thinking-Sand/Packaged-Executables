import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FileEncryptor:
    def __init__(self):
        self.salt = os.urandom(16)

    def generate_key(self, password):
        """Generate a key from the password"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return Fernet(key)

    def process_path(self, path, password, action):
        """Process a file or directory"""
        if os.path.isfile(path):
            # If it's a file, encrypt/decrypt it
            if action == "encrypt":
                return self.encrypt_file(path, password)
            else:
                return self.decrypt_file(path, password)
        elif os.path.isdir(path):
            # If it's a directory, process all files in it recursively
            success = True
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if action == "encrypt":
                            if not self.encrypt_file(file_path, password):
                                success = False
                                print(f"Failed to encrypt: {file_path}")
                        else:
                            if not self.decrypt_file(file_path, password):
                                success = False
                                print(f"Failed to decrypt: {file_path}")
                    except Exception as e:
                        success = False
                        print(f"Error processing {file_path}: {str(e)}")
            return success
        else:
            print(f"Error: Path not found: {path}")
            return False

    def encrypt_file(self, file_path, password):
        """Encrypt a file in place using the provided password"""
        try:
            # Generate encryption key from password
            fernet = self.generate_key(password)
            
            # Read the input file
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Encrypt the data
            encrypted_data = fernet.encrypt(file_data)
            
            # Write the salt and encrypted data back to the same file
            with open(file_path, 'wb') as file:
                file.write(self.salt)  # First 16 bytes will be the salt
                file.write(encrypted_data)
            
            print(f"File encrypted successfully: {file_path}")
            return True
        except Exception as e:
            print(f"Error encrypting file: {str(e)}")
            return False

    def decrypt_file(self, file_path, password):
        """Decrypt a file in place using the provided password"""
        try:
            # Read the salt and encrypted data
            with open(file_path, 'rb') as file:
                self.salt = file.read(16)  # First 16 bytes are the salt
                encrypted_data = file.read()
            
            # Generate decryption key from password
            fernet = self.generate_key(password)
            
            # Decrypt the data
            decrypted_data = fernet.decrypt(encrypted_data)
            
            # Write the decrypted data back to the same file
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
            
            print(f"File decrypted successfully: {file_path}")
            return True
        except Exception as e:
            print(f"Error decrypting file: {str(e)}")
            return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="File/Folder Encryption/Decryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("path", help="Path to the file or folder to encrypt/decrypt")
    parser.add_argument("--password", help="Encryption/Decryption password", required=True)
    
    args = parser.parse_args()
    
    encryptor = FileEncryptor()
    encryptor.process_path(args.path, args.password, args.action)
