# PRODIGY_INTERSHIP_TASK1

# Caesar Cipher Encryption Tool

Welcome to the Caesar Cipher Encryption Tool project! This project provides a tool to encrypt and decrypt messages using the Caesar Cipher.

## Description

The Caesar Cipher is a simple encryption technique where each letter in the text is shifted by a fixed number of positions in the alphabet. This project includes a Python script that allows you to encrypt or decrypt messages using this method.

## Project Structure

- `main.py`: The main script that handles the user interface and command-line argument processing.
- `cryptage.py`: Contains the Caesar encryption and decryption functions (`caesar_encryption` and `caesar_decryption`).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/FollyBoris/PRODIGY_INTERSHIP_TASK1.git
    cd PRODIGY_INTERSHIP_TASK1
    ```

2. Make sure you have Python 3 installed on your machine.

## Usage

You can use this script in two ways: via command-line arguments or via an interactive user interface.

### Using Command-Line Arguments

Run the script with the following arguments:
- `--mode`: Operation mode (`encrypt` or `decrypt`).
- `--message`: The message to encrypt or decrypt.
- `--shift`: The shift value for the Caesar Cipher.

Example:
```bash
python main.py --mode encrypt --message "Hello!" --shift 2
```
### Using Interactive Mode

If you do not provide all the necessary arguments, the script will prompt you for them interactively. This is useful if you prefer to enter information step-by-step.

Simply run the script:

bash
Copy code
python main.py
Follow the on-screen instructions:

The script will ask you to choose between encryption (1) and decryption (2).
Enter the text you want to encrypt or decrypt.
Enter the shift value (an integer) for the Caesar Cipher.
Example of interactive use:

```bash
                       __ __    ..           _____   ______    ______    ____ ____  
                     / __ __|   _          / ____/  / /  \ \  |  ____|  / ___ __ /
                    | |        | |  ____  | |      | |    | | | |____  | |______
                    | |        | | |____| | |      | |----| | |  ____|  \ ____  \ 
                    | |__ ___  | |        | |____  | |----| | | |____   ___ __| |
                     \ __ __/  |_|         \_____\ |_|    |_| |______| \ __ ___ / 

 Do you want to encrypt or decrypt a text 
 1     Encryption 
 2     Decryption 
1

 Enter your text:
Hello, World!

 Enter the shift key for the process 
3

 The encrypted messages is: Khoor, Zruog! 

                                   _____ _   _    _    _  __ _  __  _ 
                                  |_   _| | | |  / \  | |/ /| |/ / | |
                                    | | | |_| | / _ \ | ' / | ' /  | |
                                    | | |  _  |/ ___ \| . \ | . \  |_|
                                    |_| |_| |_/_/   \_\_|\_\|_|\_\ (_)
```
