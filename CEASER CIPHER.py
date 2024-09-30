print("**** CAESAR CIPHER PROGRAM ***")
# Function to encrypt the message using Caesar Cipher
def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character within the alphabet range
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabet characters are not encrypted
    
    return encrypted_message

# Function to decrypt the message
def caesar_cipher_decrypt(encrypted_message, shift):
    return caesar_cipher_encrypt(encrypted_message, -shift)

# Main Program
def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Press 'Q' to quit): ").lower()
        
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        
        elif choice == 'd':
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        
        elif choice == 'q':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
