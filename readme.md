## Encryption Assignment
This python respository was written as part of an Assignment.
This assignment makes use of AES and RSA encryption strategies to transfer a file.

## Technical Details
1. KeyGen Directory contains file which simulates the real world key distribution mechanism by generating a private and a public key and making it available to both reciever and sender
2. Sender encypts a file to be transfered to reciver using AES
3. The Sender then makes use of public key encryption(RSA) to encrypt the AES key
4. Reciever on recieving a message cipher and a key cipher uses it's own private key and decrypt the Key cipher to obtain the AES key.
5. Reciever then uses the key obtained by decryption to decrypt the message cipher.

### Running the Site Locally

To run the site locally on your own computer (most helpful for previewing your own changes), you will need to install Jekyll and other dependencies:

1. If you don't already have Python install Python2.7.
2. Next, [fork this repository](http://help.github.com/fork-a-repo/ "Instructions for Forking Your Repository") and clone it on your computer.
3. Navigate to the keyGen folder on your computer, and run the command `python keygen.py` at the command line prompt.This file will create both public and private keys and place it in the sender and reciever directories.
4. Then navigate to the sender directory, and run the command `python sender.py `.This will then generate both message and key cipher and place it in snederOp directory.
5. Then navigate to the reciever directory and run the command `python reciever.py`.This will then output the message sent by the sender in the sender Op directory.
