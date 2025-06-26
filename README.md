---

## 🖼️ Image Steganography using XOR in Python

> A simple yet effective image steganography project that hides and extracts secret messages using XOR encryption.

---

### 📌 About the Project

This project demonstrates how to securely hide a secret message inside an image using XOR-based steganography. The message is embedded into the image at the pixel level without altering its visible appearance, and it can only be decrypted using the correct encryption key.

---

### 🔐 Features

* Hide a secret message inside any image (JPG/PNG).
* Secure the message using XOR with a custom key.
* Retrieve the hidden message only if the correct key is provided.
* Works for messages of any short length.
* Supports encryption and decryption via menu input.

---

### 🚀 Technologies Used

| Tool       | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming Language          |
| OpenCV     | Image Reading & Writing       |
| NumPy      | Matrix and Pixel Manipulation |
| Matplotlib | Image Visualization           |

---

### ⚙️ How It Works

1. **Encryption**

   * The message is converted to ASCII.
   * Each character is XORed with the encryption key.
   * Resulting values are hidden in the RGB pixel values of the image.

2. **Decryption**

   * The image is read and hidden ASCII values are extracted.
   * XORed again with the same key to recover the original message.

---

### 📂 Folder Structure

```
/stegano_project
│
├── stegano.py                  # Main encryption & decryption logic
├── smiling-sun.jpg             # Original cover image
├── encrypted_output.png        # Image with hidden message
└── README.md                   # This file
```

---

### 🧪 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/image-steganography-xor.git
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python numpy matplotlib
   ```

3. Run the project:

   ```bash
   python stegano.py
   ```

4. Follow the on-screen menu:

   * Press `1` to hide a message
   * Press `2` to extract a message

---

### 📸 Screenshots

> 📌 Add these images to your repo for best results:

* `original_image.png`
* `encrypted_image.png`
* `terminal_output.png`

---

### 🔭 Future Enhancements

* Add a GUI using `Tkinter` or `PyQt5`
* Allow batch encryption of multiple images
* Add stronger encryption (AES, RSA)
* Support multimedia steganography (audio/video)

---

### 📚 References

* [OpenCV Docs](https://docs.opencv.org/)
* [NumPy Docs](https://numpy.org/doc/)
* [Matplotlib Docs](https://matplotlib.org/)
* XOR Encryption – [GeeksforGeeks](https://www.geeksforgeeks.org/xor-encryption/)

---


