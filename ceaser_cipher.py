def caesar_cipher(text, key, mode):
    result = ""
    key = key % 26  

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + key) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char  

    return result

# User input
while True:
    message = input("Enter your message: ")
    while True:
        try:
            key_value = int(input("Enter key value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the key value.")
    
    mode_input = input("Enter mode (E for encrypt / D for decrypt): ").strip().upper()
    if mode_input == 'E':
        mode = 'encrypt'
    elif mode_input == 'D':
        mode = 'decrypt'
    else:
        print("Invalid mode. Please use 'E' for encrypt or 'D' for decrypt.")
        continue
    
    if mode in ['encrypt', 'decrypt']:
        result = caesar_cipher(message, key_value, mode)
        print(f"Result: {result}")
    else:
        print("Invalid mode. Please use 'encrypt' or 'decrypt'.")
    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again != 'yes':
        break  
