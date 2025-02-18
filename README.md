# 🎭 Emotion Detector

A GUI-based Python application that displays images based on the user's entered emotion.

## 📌 Features
- User-friendly interface using **Tkinter**.
- Supports emotions like "happy", "angry", "sad", and "scary".
- Displays corresponding emotion images.
- "Reset" button to clear the input field.

## 🛠️ Requirements
Ensure you have the following installed:

- Python 3.x
- Pillow (for image handling)

### Install Dependencies:
```bash
pip install pillow
```

## 🚀 How to Run the Project
1. Clone the repository:

```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector
```

2. Run the script:

```bash
python emotion_detector.py
```

## 📂 Project Structure
```
EmotionDetector/
├── images/
│   ├── happy.jpeg
│   ├── sad.jpeg
│   ├── angry.jpeg
│   └── scary.jpeg
└── emotion_detector.py
```

Ensure your image paths are correct and match the `emotion_images` dictionary.

## 🧹 Troubleshooting
1. **ModuleNotFoundError: No module named 'PIL'**
   - Ensure **Pillow** is installed:
     ```bash
     pip install pillow
     ```

2. **Image Not Displaying**
   - Ensure the image paths are valid and images exist.

## 📌 Customization
Add new emotions by updating the `emotion_images` dictionary:

```python
emotion_images = {
    "happy": r"D:\Code\EmotionDetector\images\happy.jpeg",
    "excited": r"D:\Code\EmotionDetector\images\excited.jpeg"
}
```

## 🤝 Contributing
Feel free to fork the project and submit pull requests!

## 📧 Contact
For any questions or suggestions, reach out at [your-email@example.com](mailto:adi.upendran888@gmail.com).

