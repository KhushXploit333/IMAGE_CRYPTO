from PIL import Image
import numpy as np
from utils import encrypt_image, decrypt_image, generate_keys, load_keys

#here is stuff

def main():
    # Generate RSA keys
    generate_keys()

    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").strip().upper()
    image_path = input("Enter the path of the image: ")

    if choice == 'E':
        encrypt_image = encrypt_image(image_path)
        encrypt_image.save("encrypted_image.jpg")
        print("Image encrypted and saved as 'encrypted_image.jpg'")
    elif choice == 'D':
        decrypt_image = decrypt_image("encrypted_image.jpg")
        decrypt_image.save("decrypted_image.jpg")
        print("Image decrypted and saved as 'decrypted_image.jpg'")
    else:
        print("Invalid choice. Please choose 'E' or 'D'.")

if __name__ == "__main__":
    main()