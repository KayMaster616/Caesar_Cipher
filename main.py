
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(plain_text, shift):
    
    
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter) + shift
        cipher_text += alphabet[position]
        
    print(f"The encoded text is: {cipher_text}")
    
def decrypt(cipher_text, shift):
    
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter) - shift
        plain_text += alphabet[position]
        
    print(f"The decoded text is: {cipher_text}")
    
    
    

if __name__ == "__main__":
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
      
    if direction == "encode": 
        encrypt(text, shift) 
        
    elif direction == "decode": 
        decrypt(text, shift)
        