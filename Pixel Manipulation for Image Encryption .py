import cv2
import numpy as np

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    encrypted_image = image.copy()
    
    # Encrypt by modifying pixel values
    np.random.seed(key)
    random_matrix = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    encrypted_image = cv2.bitwise_xor(image, random_matrix)
    
    cv2.imwrite("encrypted_image.png", encrypted_image)
    print("Encryption complete. Image saved as 'encrypted_image.png'")

def decrypt_image(encrypted_image_path, key):
    encrypted_image = cv2.imread(encrypted_image_path)
    
    # Decrypt using the same key
    np.random.seed(key)
    random_matrix = np.random.randint(0, 256, encrypted_image.shape, dtype=np.uint8)
    decrypted_image = cv2.bitwise_xor(encrypted_image, random_matrix)
    
    cv2.imwrite("decrypted_image.png", decrypted_image)
    print("Decryption complete. Image saved as 'decrypted_image.png'")

# Example usage
# encrypt_image("input.png", key=1234)
# decrypt_image("encrypted_image.png", key=1234)
