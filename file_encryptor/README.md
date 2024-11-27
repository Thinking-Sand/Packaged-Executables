# File Encryptor

A secure file encryption and decryption tool that uses password-based encryption to protect your files.

## Features
- Secure file encryption using the Fernet (symmetric encryption) algorithm
- Password-based key generation with PBKDF2
- Salt-based encryption for added security
- Command-line interface for easy use

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Encrypting a file:
```
python file_encryptor.py encrypt input_file.txt encrypted_file.enc --password your_password
```

### Decrypting a file:
```
python file_encryptor.py decrypt encrypted_file.enc decrypted_file.txt --password your_password
```

## Security Features
- Uses PBKDF2 for secure key derivation
- Implements salting for protection against rainbow table attacks
- Uses the cryptography library's Fernet implementation for secure symmetric encryption

## Note
- Keep your password safe! If you lose it, you won't be able to decrypt your files
- Store encrypted files in a secure location
- The original files are not automatically deleted after encryption
