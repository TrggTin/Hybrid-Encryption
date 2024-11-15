# decryptor.py
import argparse
from main import *

def main():
    parser = argparse.ArgumentParser(description='File Decryptor')
    parser.add_argument('--receiver_private_key', required=True, help='Path to receiver\'s private key')
    parser.add_argument('--encrypted_key', required=True, help='Path to encrypted symmetric key')
    parser.add_argument('--input_file', required=True, help='Path to encrypted file')
    parser.add_argument('--output_decrypted_file', required=True, help='Path to save decrypted file')
    parser.add_argument('--sender_public_key', help='Path to sender\'s public key for verification (optional)')
    parser.add_argument('--signature', help='Path to signature file (optional)')
    
    args = parser.parse_args()

    with open(args.receiver_private_key, 'rb') as f:
        receiver_private_key = f.read()
    with open(args.encrypted_key, 'rb') as f:
        encrypted_symmetric_key = f.read()
    with open(args.input_file, 'rb') as f:
        encrypted_data = f.read()

    # giai ma aes
    symmetric_key = decrypt_symmetric_key(encrypted_symmetric_key, receiver_private_key)

    # giai ma file
    decrypted_data = decrypt_file(encrypted_data, symmetric_key)

    # Save decrypted file
    with open(args.output_decrypted_file, 'wb') as f:
        f.write(decrypted_data)

    # Verify file integrity if sender's public key and signature are provided
    if args.sender_public_key and args.signature:
        with open(args.sender_public_key, 'rb') as f:
            sender_public_key = f.read()
        with open(args.signature, 'rb') as f:
            signature = f.read()

        is_valid = verify_signature(encrypted_data, signature, sender_public_key)
        print("FILE IS VALID" if is_valid else "FILE IS INVALID")

if __name__ == '__main__':
    main()