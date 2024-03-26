import random
import re

def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        word = word[1:] + first_letter
        random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return random_chars + word + random_chars
    else:
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        random_chars = word[:3]
        word = word[3:-3]
        last_letter = word[-1]
        word = last_letter + word[:-1]
        return word

def encode_message(message):
    words = re.findall(r'\b\w+\b', message)
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    choice = input("Do you want to code or decode? (Enter 'code' or 'decode'): ").lower()
    if choice == 'code':
        message = input("Enter the message to encode: ")
        encoded_message = encode_message(message)
        print("Encoded message:", encoded_message)
    elif choice == 'decode':
        message = input("Enter the message to decode: ")
        decoded_message = decode_message(message)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice. Please enter 'code' or 'decode'.")

if __name__ == "__main__":
    main()
