```bash
python main.py

python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=file_to_encrypt.txt --output_encrypted_file=encrypted_file.txt --output_encrypted_symmetric_key=encrypted_key.key

python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=encrypted_file.txt --output_decrypted_file=decrypted_txt.txt
```

```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=file_to_encrypt.jpg --output_encrypted_file=encrypted_file.enc --output_encrypted_symmetric_key=encrypted_key.key

python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=encrypted_file.enc --output_decrypted_file=decrypted_jpg.jpg
```

```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=lab00-encryption.pdf --output_encrypted_file=pdf.enc --output_encrypted_symmetric_key=encrypted_key.key

python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=pdf.enc --output_decrypted_file=decrypted_pdf.jpg
```

```bash
python encryptor.py --receiver_pub_key=receiver_pub_key.pub --input_file=file_to_encrypt.txt --output_encrypted_file=encrypted_file.txt --output_encrypted_symmetric_key=encrypted_key.key --sender_private_key=sender_private_key.key --output_signature=signature.sig 

python decryptor.py --receiver_private_key=receiver_private_key.key --encrypted_key=encrypted_key.key --input_file=encrypted_file.txt --output_decrypted_file=decrypted_file.txt --sender_public_key=sender_pub_key.pub --signature=signature.sig
```