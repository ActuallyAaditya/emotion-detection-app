import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from textblob import TextBlob


def detect_emotion():
    text = text_entry.get("1.0", 'end-1c')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiment_perc = float("{:.2f}".format(abs(sentiment * 100)))
    if text == "":
        emotion_label.config(text=f"Text field is empty. Please enter some text", foreground="black", font=('Helvetica', 14))
    elif sentiment > 0:
        emotion_label.config(text=f"😊 Positive sentiment: {sentiment_perc}%", foreground="green")
    elif sentiment < 0:
        emotion_label.config(text=f"😞 Negative sentiment: {sentiment_perc}%", foreground="red")
    else:
        emotion_label.config(text=f"😐 Neutral sentiment: {sentiment_perc}%", foreground="black")


def detect_emotion_input(content):
    text = content
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiment_perc = float("{:.2f}".format(abs(sentiment * 100)))
    if text == "":
        emotion_label.config(text=f"Text field is empty. Please enter some text", foreground="black", font=('Helvetica', 14))
    elif sentiment > 0:
        emotion_label.config(text=f"😊 Positive sentiment: {sentiment_perc}%", foreground="green")
    elif sentiment < 0:
        emotion_label.config(text=f"😞 Negative sentiment: {sentiment_perc}%", foreground="red")
    else:
        emotion_label.config(text=f"😐 Neutral sentiment: {sentiment_perc}%", foreground="black")


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            detect_emotion_input(content)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")


def exit_app():
    root.destroy()


def show_about():
    messagebox.showinfo("About This Project",
                        "This project uses NLP techniques to detect and classify emotions within textual data and categorizes them into positive, neutral and negative statements.")


def start_detection():
    menu_frame.pack_forget()  # Hide the main menu frame
    detection_frame.pack(pady=20)  # Show the detection frame


def go_back():
    detection_frame.pack_forget()  # Hide the detection frame
    menu_frame.pack(pady=20)  # Show the main menu frame


# Create the main window
root = tk.Tk()
root.title("Emotion Detector")

# Main menu frame
menu_frame = tk.Frame(root, height=270, width=400)
menu_frame.pack_propagate(0)
menu_frame.pack(pady=20, anchor="center")

title_label = tk.Label(menu_frame, text="Emotion Detection App", font=('Helvetica', 20, 'bold'))
title_sub_label = tk.Label(menu_frame,text="Detects the sentiments of a text", font=('Helvetica', 12, 'bold'))
title_label.pack(pady=0)
title_sub_label.pack(ipady=20)

start_button = tk.Button(menu_frame, text="Start", command=start_detection,
                         height=2,
                         width=11,
                         font=('Helvetica', 12),
                         bg="#6a994e",
                         fg='white',
                         bd=0,
                         relief="flat",
                         activebackground="#386641",
                         activeforeground="white")
start_button.pack(pady=2)

about_button = tk.Button(menu_frame, text="About", command=show_about,
                         height=2,
                         width=11,
                         font=('Helvetica', 12),
                         bg="#2196F3",
                         fg='white',
                         bd=0,
                         relief="flat",
                         activebackground="#0D47A1",
                         activeforeground="white")
about_button.pack(pady=2)

exit_button = tk.Button(menu_frame, text="Exit", command=exit_app,
                        height=2,
                        width=11,
                        font=('Helvetica', 12),
                        bg="#c1121f",
                        fg='white',
                        bd=0,
                        relief="flat",
                        activebackground="#780000",
                        activeforeground="white")
exit_button.pack(pady=2)

# Detection screen frame
detection_frame = tk.Frame(root, height=400, width=400)
detection_frame.pack_propagate(0)  # prevent resizing

# Text entry widget
text_entry = tk.Text(detection_frame, height=10, width=50, font=('Helvetica', 12))
text_entry.pack(pady=10)

# Button to trigger emotion detection
detect_button = tk.Button(detection_frame, text="Detect Emotion", command=detect_emotion,
                          height=2,
                          width=14,
                          font=('Helvetica', 12),
                          bg="#6a994e",
                          fg='white',
                          bd=0,
                          relief="flat",
                          activebackground="#386641",
                          activeforeground="white")
detect_button.pack(pady=11)

open_button = tk.Button(detection_frame, text="Open Text File", command=open_file,
                        height=2,
                        width=14,
                        font=('Helvetica', 12),
                        bg="#2196F3",
                        fg='white',
                        bd=0,
                        relief="flat",
                        activebackground="#0D47A1",
                        activeforeground="white")
open_button.pack()

# Label to display emotion
emotion_label = tk.Label(detection_frame, text="", font=('Helvetica', 18))
emotion_label.pack(pady=10)

# Button to go back to the main menu frame
back_button = tk.Button(detection_frame, text="Back", command=go_back,
                        height=2,
                        width=8,
                        font=('Helvetica', 12),
                        bg="#c1121f",
                        fg='white',
                        bd=0,
                        relief="flat",
                        activebackground="#780000",
                        activeforeground="white")
back_button.pack(pady=1)

# Run the main event loop
root.mainloop()
