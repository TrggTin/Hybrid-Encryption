import hashlib

def demonstrate_hashing():
    # Example 1: Same data produces same hash
    message1 = b"Hello, World!"
    message2 = b"Hello, World!"
    
    hash1 = hashlib.sha256(message1).digest()
    hash2 = hashlib.sha256(message2).digest()
    
    print("Example 1: Same data, same hash")
    print(f"Hash1: {hash1.hex()}")
    print(f"Hash2: {hash2.hex()}")
    print(f"Hashes are equal: {hash1 == hash2}")
    
    # Example 2: Slightly different data produces completely different hash
    message3 = b"Hello, World"  # Removed '!'
    hash3 = hashlib.sha256(message3).digest()
    
    print("\nExample 2: Different data, different hash")
    print(f"Hash1: {hash1.hex()}")
    print(f"Hash3: {hash3.hex()}")
    print(f"Hashes are equal: {hash1 == hash3}")
    
    # Example 3: Demonstrate file hashing
    def hash_file_content(content):
        return hashlib.sha256(content).digest()
    
    original_file = b"This is my important file content"
    modified_file = b"This is my important file content."  # Added period
    
    print("\nExample 3: File hashing")
    print(f"Original file hash: {hash_file_content(original_file).hex()}")
    print(f"Modified file hash: {hash_file_content(modified_file).hex()}")

# Run the demonstration
demonstrate_hashing()