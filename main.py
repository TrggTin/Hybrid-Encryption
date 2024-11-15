#File set up
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import hashlib
from base64 import b64encode, b64decode

#Tao khoa cap khoa private - public RSA
def generate_key(bits=2048):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.public_key().export_key()
    return private_key, public_key

#Tao khoa doi xung 
def generate_symmetric_key(bytes):
    return get_random_bytes(bytes)

#Ma hoa khoa doi xung 
def encrypt_symmetric_key(synmetric_key, public_key):
    #Nguoi nhan gui Public key
    recipent_key = RSA.import_key(public_key)

    #Ma hoa khoa doi xung voi Public key cua nguoi nhan
    cipher_rsa = PKCS1_OAEP.new(recipent_key)
    encrypt_synmetric_key = cipher_rsa.encrypt(synmetric_key)
    return encrypt_synmetric_key

def decrypt_symmetric_key(enc_symmetric_key, private_key):
    """Decrypt symmetric key using RSA private key"""
    recipient_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    symmetric_key = cipher_rsa.decrypt(enc_symmetric_key)
    return symmetric_key

#Ma hoa file
def encrypt_file(input_file, synmetric_key):
    #Ma hoa voi khoa doi xung
    #vector khoi tao khi chay voi cipher block chaining luon = 16 bytes bat ke key size la bao nhieu
    iv = get_random_bytes(16)
    cipher = AES.new(synmetric_key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        file_data = f.read()

    #Xử lí dữ liệu để đủ bytes đọc cho file nếu thiếu dữ liệu (do giải mã và mã hóa đều đọc theo một khối bytes)
    #Pad data
    padded_data = pad(file_data, AES.block_size)

    #Ma hoa
    encrypted_data = cipher.encrypt(padded_data)

    return iv + encrypted_data

def decrypt_file(encrypted_data, symmetric_key):
    #Giai ma file
    #Loai tru iv ra khoi file (16 bytes dau)
    iv = encrypted_data[:16]
    cipher = AES.new(symmetric_key, AES.MODE_CBC, iv)
    
    #Giai ma
    decrypted_padded_data = cipher.decrypt(encrypted_data[16:])
    
    #tra lai so luong bytes ban dau truoc khi padding
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)
    
    return decrypted_data

def calculate_file_hash(file_data):
    #Tao fingerprint cho file qua ham bam sha256
    return SHA256.new(file_data)

def sign_hash(file_hash, private_key):
    #Xac dinh ki ten fingerprint = private key cua nguoi gui
    signer_key = RSA.import_key(private_key)
    signer = pkcs1_15.new(signer_key)
    signature = signer.sign(file_hash)
    return signature

def verify_signature(file_data, signed_hash, public_key):
    #Xac thuc lai file fingerprint = public key cua nguoi nhan 
    calculated_hash = calculate_file_hash(file_data)
    verifier_key = RSA.import_key(public_key)
    verifier = pkcs1_15.new(verifier_key)
    try:
        verifier.verify(calculated_hash, signed_hash)
        return True
    except (ValueError, TypeError):
        return False
    
def main():
    # Tao cap khoa cua reiceiver và ghi vao file --> khoa nay do receiver su dung
    private_key, public_key = generate_key()
    with open('receiver_private_key.key', 'wb') as f:
        f.write(private_key)
    with open('receiver_pub_key.pub', 'wb') as f:
        f.write(public_key)

    # Tao cap khoa do sender và ghi vao file --> khoa nay do sender su dung va duoc dung de tao file xac thuc 
    sender_private_key, sender_public_key = generate_key()
    with open('sender_private_key.key', 'wb') as f:
        f.write(sender_private_key)
    with open('sender_pub_key.pub', 'wb') as f:
        f.write(sender_public_key)

    #Testing lúc code 
    # #Key duoc tao ra va neu xuat ra se doc o dang nhi phan --> not readable
    # print(private_key.decode())
    # print("\n")
    # print(public_key.decode())
    # print("\n")
    # syn_key = generate_symmetric_key(32)
    # print(syn_key.hex())
    # print("\n")
    # enc_syn_key = encrypt_symmetric_key(syn_key, public_key)
    # print(enc_syn_key.hex())

if __name__ == "__main__":
    main()