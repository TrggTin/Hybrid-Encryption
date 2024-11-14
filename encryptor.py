import argparse
from main import *

def main():
    parser = argparse.ArgumentParser(description='File Encryptor')
    parser.add_argument('--receiver_pub_key', required=True, help='Path to receiver\'s public key file')
    parser.add_argument('--input_file', required=True, help='Path to file to encrypt')
    parser.add_argument('--output_encrypted_file', required=True, help='Path to save encrypted file')
    parser.add_argument('--output_encrypted_symmetric_key', required=True, help='Path to save encrypted symmetric key')
    parser.add_argument('--sender_private_key', help='Path to sender\'s private key for signing (optional)')
    parser.add_argument('--output_signature', help='Path to save signature (optional)')
    
    args = parser.parse_args()

    # đọc khóa pub của người nhận 
    with open(args.receiver_pub_key, 'rb') as f:
        receiver_public_key = f.read()

    # tạo khóa đối xứng 
    symmetric_key = generate_symmetric_key(32)

    # mã hóa khóa đối xứng với pub key của người nhận --> encrypted sym key 
    encrypted_symmetric_key = encrypt_symmetric_key(symmetric_key, receiver_public_key)

    # mã hóa 
    encrypted_data = encrypt_file(args.input_file, symmetric_key)

    # lưu encrypted sym key
    with open(args.output_encrypted_symmetric_key, 'wb') as f:
        f.write(encrypted_symmetric_key)

    # lưu encrypted file
    with open(args.output_encrypted_file, 'wb') as f:
        f.write(encrypted_data)

    # xac thuc file thong qua private key cua nguoi gui (neu co)
    if args.sender_private_key and args.output_signature:
        with open(args.sender_private_key, 'rb') as f:
            sender_private_key = f.read()
        
        file_hash = calculate_file_hash(encrypted_data)
        signature = sign_hash(file_hash, sender_private_key)
        
        with open(args.output_signature, 'wb') as f:
            f.write(signature)

if __name__ == '__main__':
    main()