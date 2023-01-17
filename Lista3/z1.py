import base64 as crypto
import random

# Base64 cryptographic part
def encode_base64(any_bytes_sequence):
    return crypto.b64encode(any_bytes_sequence)
    
def decode_base64(base64_bytes_sequence):
    return crypto.b64decode(base64_bytes_sequence)

# Testing
def test_b64_encode_decode_functions():
    def generate_random_bytes_sequence(length):
        return bytes([random.randint(0, 255) for _ in range(length)])
    
    number_of_tests = 1000
    max_length = 1000
    bytes_sequences_lengths = [random.randint(0, max_length) for _ in range(number_of_tests)]
    for seq_length in bytes_sequences_lengths:
        test_candidate = generate_random_bytes_sequence(seq_length)
        encoded_candidate = encode_base64(test_candidate)
        decoded_encoded_candidate = decode_base64(encoded_candidate)
        assert test_candidate == decoded_encoded_candidate

# UTF-8 support for any character based passwords
def encode_password(pwd):
    return encode_base64(bytes(pwd, 'UTF-8')).decode("utf-8")

def decode_password(pwd):
    return decode_base64(bytes(pwd, 'UTF-8')).decode("utf-8")

if __name__ == "__main__":
    my_raw_password = "$up3r_Trudn3_Hasl0"
    my_encoded_password = encode_password(my_raw_password)
    my_decoded_encoded_password = decode_password(my_encoded_password)
    print(f"My Extranet password: {my_raw_password}")
    print(f"My Extranet encoded password: {my_encoded_password}")
    print(f"My Extranet decrypted password: {my_decoded_encoded_password}")
    
    # Run tests
    test_b64_encode_decode_functions()
    