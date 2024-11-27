# File Encryptor

A secure file encryption and decryption tool that uses password-based encryption to protect your files/folders

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
Click on encrypt.bat it will ask you for the path to file, type/copy the path or drop the file/folder into the terminal and hit enter. 
It will then ask you for a password, once that's done your file/folder and its contents are encrypted.



### Decrypting a file:
Click on decrypt.bat it will ask you for the path to file, type/copy the path or drop the file/folder into the terminal and hit enter. 
It will then ask you for your password you entered, once that's done your file/folder and its contents are decrypted.



## Security Features
- Uses PBKDF2 for secure key derivation
- Implements salting for protection against rainbow table attacks
- Uses the cryptography library's Fernet implementation for secure symmetric encryption

## Note
- Keep your password safe! If you lose it, you won't be able to decrypt your files
- Store encrypted files in a secure location
- This does not copy your file/folder, Once encrypted it will stay that way until you enter your password.
- Make a .txt file to test it out and get the feel for it.