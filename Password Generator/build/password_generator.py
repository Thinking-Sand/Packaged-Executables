import random
import string
import pyperclip  # For copy to clipboard (install with: pip install pyperclip)

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate_passwords(self, length, count, use_upper=True, use_lower=True, 
                         use_numbers=True, use_symbols=True):
        # Build character set based on user preferences
        chars = ''
        if use_lower:
            chars += self.lowercase
        if use_upper:
            chars += self.uppercase
        if use_numbers:
            chars += self.numbers
        if use_symbols:
            chars += self.symbols

        # Ensure at least one character set is selected
        if not chars:
            return ["Error: Please select at least one character type!"]

        # Generate multiple passwords
        passwords = []
        for _ in range(count):
            password = ''.join(random.choice(chars) for _ in range(length))
            passwords.append(password)
        
        return passwords

def main():
    generator = PasswordGenerator()
    
    print("\n🔐 Advanced Password Generator 🔐\n")
    
    try:
        # Get user preferences
        length = int(input("Password length (8-50): "))
        if not 8 <= length <= 50:
            print("Please choose a length between 8 and 50!")
            return

        count = int(input("Number of passwords to generate (1-10): "))
        if not 1 <= count <= 10:
            print("Please choose between 1 and 10 passwords!")
            return

        # Get complexity preferences
        print("\nPassword complexity options:")
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate and display passwords
        print("\n📋 Generated Passwords:")
        print("-" * 50)
        
        passwords = generator.generate_passwords(
            length, count, use_upper, use_lower, use_numbers, use_symbols
        )

        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")

        # Ask if user wants to copy a specific password
        if len(passwords) > 0:
            print("\nWould you like to copy a password to clipboard?")
            choice = input(f"Enter password number (1-{len(passwords)}) or 'n' to exit: ")
            if choice.isdigit() and 1 <= int(choice) <= len(passwords):
                pyperclip.copy(passwords[int(choice)-1])
                print("✅ Password copied to clipboard!")

    except ValueError:
        print("❌ Please enter valid numbers!")
    except KeyboardInterrupt:
        print("\n\nPassword generation cancelled.")

if __name__ == "__main__":
    main()