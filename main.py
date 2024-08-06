from cryptage import caesar_decryption, caesar_encryption
import argparse

def main():
    try:
        print("""
                       __ __    ..           _____   ______    ______    ____ ____  
                     / __ __|   _          / ____/  / /  \ \  |  ____|  / ___ __ /
                    | |        | |  ____  | |      | |    | | | |____  | |______
                    | |        | | |____| | |      | |----| | |  ____|  \ ____  \ 
                    | |__ ___  | |        | |____  | |----| | | |____   ___ __| |
                     \ __ __/  |_|         \_____\ |_|    |_| |______| \ __ ___ / 
""" )
        
        # take the argument directly if the user launch python main.py --mode encrypt --message "Hello!" --shift 2
        parser = argparse.ArgumentParser(description="Caesar Cipher Encryption Tool")
        parser.add_argument("--mode", choices=["encrypt", "decrypt"], help="Mode of operation")
        parser.add_argument("--message", help="Message to encrypt or decrypt")
        parser.add_argument("--shift", type=int, help="Shift value for the Caesar Cipher")
        args = parser.parse_args()
        
        # verify if all argument are present
        if not args.mode and not args.message and not args.shift:
            # take the user choice, encrypt or decrypt
            choice = int(input(" Do you want to encrypt or decrypt a text \n 1     Encryption \n 2     Decryption \n"))
            
            # verify the user option is correct
            if choice == 1 or choice == 2:
                
                # take the plaintext for encryption or the caesar text for decryption
                
                text = str(input("\n Enter your text:\n"))
                
                #take the shift key
                shift_key = int(input("\n Enter the shift key for the process \n"))
                
                # start process //encryption or //decryption
                if choice == 1:
                    print(f" The encrypted messages is: {caesar_encryption(text, shift_key)} ")
                else :
                    print(f" The encrypted messages is: {caesar_decryption(text, shift_key)} ")
        # if one of the args is miss said to the user to provide it
        if not args.mode:
            print("Error: --mode argument is required")
        elif not args.message:
            print("Error: --message argument is required")
        elif args.shift is None:
            print("Error: --shift argument is required")
        else:
            # If all args are present start
            # Depending of the users choose mode the program start the appropriate option
            if args.mode=="encrypt":
                print(f"\n The message to encrypt is : {args.message} \n The encrypted messages is: {caesar_encryption(args.message, args.shift)} ")
            else :
                print(f"\n The message to decrypt is : {args.message} \n The decrypted messages is: {caesar_decryption(args.message, args.shift)} ")
            
        
        print("""
                                   _____ _   _    _    _  __ _  __  _ 
                                  |_   _| | | |  / \  | |/ /| |/ / | |
                                    | | | |_| | / _ \ | ' / | ' /  | |
                                    | | |  _  |/ ___ \| . \ | . \  |_|
                                    |_| |_| |_/_/   \_\_|\_\|_|\_\ (_)
""")
                
    except Exception as e:
        print(f" The error is {e}")
        

if __name__ == "__main__":
        main()
        
    