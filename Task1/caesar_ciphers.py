# characters encryption or decryption using caesar cipher logics 
def caesar_ciphers(char, shift, mode="encrypt"):
    
    if mode =="decrypt":
        shift = -shift
    
    # Encrypt or Decrypt characters
    if char.isupper() or char.islower():
        base_asci = 65 if char.isupper() else 97
        result = chr((ord(char) + shift - base_asci) % 26 + base_asci)
        
    # Ignore character if it is not a letter and leave it as it is
    else:
        result = char
    
    return result
