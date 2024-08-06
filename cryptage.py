from caesar_ciphers import caesar_ciphers

# plaintext encryption
def caesar_encryption(text, shift):  
    try:     
        message = ''
        for char in text:
            result = caesar_ciphers(char=char,shift=shift)
            
            message +=result
        
        return message
            
    except Exception as e:
        print(f"Encryption Error {e}")


 #caesar cipher_text decryption 
def caesar_decryption(cipher_text, shift):
    try:     
        message = ''
        for char in cipher_text:
            result = caesar_ciphers(char=char,shift=shift, mode="decrypt")
            message +=result
        
        return message
            
    except Exception as e:
        print(f"Decryption Error {e}")
 
  