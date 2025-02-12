# Caesar Cipher Encryption Program

## Description
This is a simple Python program that implements the Caesar cipher encryption technique. The program allows users to encrypt and decrypt messages using a specified shift value.

## How It Works
1. The user is prompted to choose between encoding (encryption) or decoding (decryption).
2. The user enters the message they want to process.
3. The user specifies the shift number, which determines how many positions each letter moves in the alphabet.
4. The program shifts each letter accordingly and outputs the encoded or decoded message.

## Features
- Encrypts messages by shifting letters forward in the alphabet.
- Can be extended to support decryption.
- Simple and easy-to-use command-line interface.

## Usage
Run the program in a Python environment and follow the prompts:

```python
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
The encoded text is: mjqqt
```

## Known Issues
- The program currently does not handle spaces, numbers, or special characters.
- The decryption functionality is not implemented yet.
- It uses a redundant alphabet list instead of handling index wrapping more efficiently.

## Future Improvements
- Implement decryption.
- Improve handling of spaces, numbers, and special characters.
- Optimize the algorithm to avoid using duplicate alphabet entries.

## License
This project is open-source and free to use.

