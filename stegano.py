# 🔹 Step 1: Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 🔹 Step 2: ASCII conversion dictionaries
d = {chr(i): i for i in range(255)}  # character → ASCII
c = {i: chr(i) for i in range(255)}  # ASCII → character

# 🔹 Step 3: Encryption function
def encrypt_image():
    image_path = r"D:\Project Internship\smiling-sun.jpg"  # Use a PNG or JPG instead of WEBP
    text = "Abhishek"
    key = "123"
    output_image_path = "encrypted_output.png"

    # Check if file exists
    if not os.path.exists(image_path):
        print("❌ Image file not found at:", image_path)
        return

    x = cv2.imread(image_path)

    if x is None:
        print("❌ Failed to load the image. Try using a PNG or JPG image.")
        return

    x_enc = x.copy()
    n, m, z = 0, 0, 0
    kl = 0
    l = len(text)

    for i in range(l):
        new_val = d[text[i]] ^ d[key[kl]]
        x_enc[n, m, z] = new_val

        print(f"[+] Embedding '{text[i]}' XOR '{key[kl]}' = {new_val} at pixel ({n},{m},{z})")

        n = (n + 1) % x_enc.shape[0]
        m = (m + 1) % x_enc.shape[1]
        z = (z + 1) % 3
        kl = (kl + 1) % len(key)

    cv2.imwrite(output_image_path, x_enc)
    print(f"\n✅ Encrypted image saved as: {output_image_path}")

    x_rgb = cv2.cvtColor(x_enc, cv2.COLOR_BGR2RGB)
    plt.imshow(x_rgb)
    plt.axis('off')
    plt.title("Encrypted Image")
    plt.show()

# 🔹 Step 4: Decryption function
def decrypt_image():
    image_path = "encrypted_output.png"
    key = "123"
    message_length = 8  # 'Abhishek'

    if not os.path.exists(image_path):
        print("❌ Encrypted image not found at:", image_path)
        return

    x = cv2.imread(image_path)

    if x is None:
        print("❌ Failed to load encrypted image.")
        return

    n, m, z = 0, 0, 0
    kl = 0
    decrypted_text = ""

    for i in range(message_length):
        hidden_val = x[n, m, z]
        original_char = hidden_val ^ d[key[kl]]
        decrypted_text += c[original_char]

        print(f"[+] Extracted {hidden_val} XOR '{key[kl]}' = '{c[original_char]}' at pixel ({n},{m},{z})")

        n = (n + 1) % x.shape[0]
        m = (m + 1) % x.shape[1]
        z = (z + 1) % 3
        kl = (kl + 1) % len(key)

    print("\n🔓 Decrypted Message:", decrypted_text)

# 🔹 Step 5: Main menu
def main():
    print("\n🔐 XOR Image Steganography Tool")
    print("1. Encrypt the message 'Abhishek' into the image")
    print("2. Decrypt message from the image")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        encrypt_image()
    elif choice == "2":
        decrypt_image()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

# 🔹 Step 6: Run the program
if __name__ == "__main__":
    main()
