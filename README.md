# Hybrid Encryption System Installation Guide

## Requirements
- Python 3.7 or higher
- pycryptodome library

## Installation Steps

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install pycryptodome
```

## Usage

### 1. Generate Key Pairs

### 2. Encrypt a File
Basic encryption:
```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=file_to_encrypt.txt --output_encrypted_file=encrypted_file.txt --output_encrypted_symmetric_key=encrypted_key.key
```

With file integrity verification:
```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=file_to_encrypt.txt --output_encrypted_file=encrypted_file.txt --output_encrypted_symmetric_key=encrypted_key.key --sender_private_key=sender_private_key.key --output_signature=signature.sig
```

### 3. Decrypt a File
Basic decryption:
```bash
python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=encrypted_file.txt --output_decrypted_file=decrypted_file.txt
```

With file integrity verification:
```bash
python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=encrypted_file.txt --output_decrypted_file=decrypted_file.txt --sender_public_key=sender_pub_key.pub --signature=signature.sig
```

## Supported File Types
The system supports all file types as it operates on binary data. Tested file types include:
- Text files (.txt)
- Image files (.png, .jpg, .jpeg)
- PDF files (.pdf)
- And more...

## Implementation Details
- RSA key size: 2048 bits
- AES key size: 256 bits
- AES mode: CBC with PKCS7 padding
- Hash algorithm: SHA-256
- RSA padding: PKCS1_OAEP