from PIL import Image
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key)

def load_keys():
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
    with open("public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())
    return private_key, public_key

def xor_operation(data, key):
    """Perform XOR operation between data and key."""
    return bytes([b ^ key for b in data])

def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Convert pixel values to bytes
    pixel_data = pixels.tobytes()

    # Load public key
    _, public_key = load_keys()

    # Encrypt pixel data
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(pixel_data)

    # Save encrypted data to a file
    with open("encrypted_data.bin", "wb") as f:
        f.write(encrypted_data)

    # Manipulate pixels using XOR operation
    key = 123  # Example XOR key
    manipulated_pixels = xor_operation(pixel_data, key)

    # Convert manipulated bytes back to an image
    manipulated_image = Image.frombytes(image.mode, image.size, manipulated_pixels)
    return manipulated_image

def decrypt_image(image_path):
    # Load private key
    private_key, _ = load_keys()

    # Read encrypted data
    with open("encrypted_data.bin", "rb") as f:
        encrypted_data = f.read()

    # Decrypt pixel data
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Convert bytes back to pixel array
    height, width = Image.open(image_path).size
    pixels = np.frombuffer(decrypted_data, dtype=np.uint8).reshape((height, width, 3))

    # Reverse XOR operation
    key = 123  # Same XOR key used during encryption
    original_pixels = xor_operation(decrypted_data, key)

    # Convert bytes back to an image
    original_image = Image.frombytes(Image.open(image_path).mode, Image.open(image_path).size, original_pixels)
    return original_image


# USAGE
image_path = r"C:\Users\Khushbu\Desktop\IMAGE CRYPTOGYAPHY\input.jpg"
encrypt_image = r"C:\Users\Khushbu\Desktop\IMAGE CRYPTOGYAPHY\encrypt.jpg"
decrypt_image = r"C:\Users\Khushbu\Desktop\IMAGE CRYPTOGYAPHY\decrypt.jpg"