import tkinter as tk
from tkinter import messagebox
from PIL import  Image, ImageTk

emotion_image={
    "happy": r"D:\Code\EmotionDetector\images\happy.jpeg",

    "angry": r"D:\Code\EmotionDetector\images/angry.jpeg",
    "sad": r"D:\Code\EmotionDetector\images/sad.jpeg",
    "scary":r"D:\Code\EmotionDetector\images/scary.jpeg",
}

def show_emotion():
    emotion = emotion_entry.get().strip().lower()

    if emotion in emotion_image:
        image_window = tk.Toplevel(root)
        image_window.title(f"You are feeling {emotion.capitalize()}")

        img_path =emotion_image[emotion]

        try:
            img= Image.open(img_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img= ImageTk.PhotoImage(img)

            label= tk.Label(image_window,image=img)
            label.imaeg=img
            label.pack()
        
        except Exception as e:
            messagebox.showerror("error",f"Could not load image: {e}")
    
    else:
        messagebox.showwarning("Unknown Emotion", f"Emotion '{emotion}' not recognized!")

def reset():
    emotion_entry.delete(0,tk.END)

root= tk.Tk()
root.title("Emotion Detector")
root.geometry("400x200")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Label row
emotion_label = tk.Label(root, text="Enter your emotion:", font=("Arial", 14))
emotion_label.grid(row=0, column=0, columnspan=2, pady=10)

# Text entry row
emotion_entry = tk.Entry(root, font=("Arial", 14), width=30)
emotion_entry.grid(row=1, column=0, columnspan=2, pady=10)

# Buttons row
detect_button = tk.Button(root, text="Your Emotion", font=("Arial", 12), command=show_emotion)
detect_button.grid(row=2, column=0, padx=20, pady=20)

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset)
reset_button.grid(row=2, column=1, padx=20, pady=20)

# Run the GUI
root.mainloop()