import tkinter as tk
from tkinter import Label, Canvas
import pyttsx3  # For better TTS
import pygame
from PIL import Image, ImageTk
import os

# Initialize pygame mixer for playing audio
pygame.mixer.init()

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 200)  # Set decent speed for TTS

class VideoPlayer(tk.Tk):
    def __init__(self, videos):
        super().__init__()
        self.videos = videos
        self.current_index = 0
        self.step_index = 0

        # Window configuration
        self.geometry("800x600")
        self.title("Shorts Video Player")

        # Set a custom background color for appealing visuals
        self.configure(bg="#2c3e50")

        # Canvas for displaying video (text + key info like equations)
        self.canvas = Canvas(self, width=800, height=400, bg="#ecf0f1")
        self.canvas.pack(pady=20)

        # Label for showing key info, centered, and appealing font
        self.info_label = Label(self, text="", font=("Helvetica", 24), fg="white", bg="#2c3e50")
        self.info_label.pack(pady=20)

        # Bind key events for scrolling
        self.bind("<Up>", self.scroll_up)
        self.bind("<Down>", self.scroll_down)

        # Trigger window close to perform cleanup
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Load the first video
        self.play_video()

    def play_video(self):
        video = self.videos[self.current_index]

        # Play music only when the video starts (first step)
        if self.step_index == 0 and video['music']:
            pygame.mixer.music.load(video['music'])
            pygame.mixer.music.play(-1)  # -1 for looping the background music

        # Show key information (e.g., equations)
        self.display_info(video['key_info'][self.step_index], video['visuals'][self.step_index])

        # Play the current step of the script with text-to-speech
        self.play_tts(video['script'][self.step_index])

        # Automatically advance to the next step after a delay
        self.after(2000, self.next_step)  # Change step every 2 seconds

    def next_step(self):
        video = self.videos[self.current_index]

        # Move to the next step
        if self.step_index < len(video['script']) - 1:
            self.step_index += 1
            self.play_video()
        elif self.current_index < len(self.videos) - 1:
            self.current_index += 1
            self.step_index = 0
            self.play_video()

    def play_tts(self, text):
        # Speak the text with the pyttsx3 engine
        tts_engine.say(text)
        tts_engine.runAndWait()

    def display_info(self, info, visual):
        # Clear previous items from canvas
        self.canvas.delete("all")

        # Display key information (image or text)
        if visual and os.path.exists(visual):
            img = Image.open(visual)
            img = img.resize((400, 400), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(img)
            self.canvas.create_image(400, 200, image=self.img)  # Center image in canvas
        else:
            self.info_label.config(text=info, anchor="center")  # Center the text info

    def scroll_up(self, event):
        if self.step_index > 0:
            self.step_index -= 1
            self.play_video()
        elif self.current_index > 0:
            self.current_index -= 1
            self.step_index = 0
            self.play_video()

    def scroll_down(self, event):
        video = self.videos[self.current_index]
        if self.step_index < len(video['script']) - 1:
            self.step_index += 1
            self.play_video()
        elif self.current_index < len(self.videos) - 1:
            self.current_index += 1
            self.step_index = 0
            self.play_video()

    def on_close(self):
        # Stop music when closing
        pygame.mixer.music.stop()

        # Cleanup generated files if any
        if os.path.exists("speech.mp3"):
            os.remove("speech.mp3")
        
        # Exit application
        self.destroy()

# Sample video data (Script, Music, Key Information, and Visuals)
videos = [
    {
        "script": [
            "Let's begin with solving the quadratic equation step-by-step.",
            "First, the quadratic formula is x equals negative b plus or minus the square root of b squared minus 4ac over 2a.",
            "Now, let's substitute the values into the formula. If a is 1, b is 3, and c is -4...",
            "We get x equals negative 3 plus or minus the square root of 9 plus 16 over 2.",
            "Finally, solving it gives x equals 1 and x equals -4."
        ],
        "music": "C:\\Users\\Mdanm\\Downloads\\Python Practise\\Youtube_Videos\\saitama_lofi.mp3",
        "key_info": [
            "Step 1: Write down the quadratic formula.",
            "Step 2: Substitute values into the formula.",
            "Step 3: Simplify the expression.",
            "Step 4: Solve for x using square root.",
            "Final result: x = 1, x = -4"
        ],
        "visuals": [
            "C:\\path_to_images\\quadratic_formula.png",
            "C:\\path_to_images\\quadratic_substitution.png",
            "C:\\path_to_images\\quadratic_simplification.png",
            "C:\\path_to_images\\quadratic_solution.png",
            "C:\\path_to_images\\quadratic_final_result.png"
        ]
    },
    {
        "script": ["This is the first video explaining Pythagoras theorem."],
        "music": "C:\\Users\\Mdanm\\Downloads\\Python Practise\\Youtube_Videos\\saitama_lofi.mp3",
        "key_info": ["a^2 + b^2 = c^2"],
        "visuals": ["C:\\path_to_images\\pythagorean_theorem.png"]
    },
    {
        "script": ["Here we talk about Euler's formula in complex numbers."],
        "music": "C:\\Users\\Mdanm\\Downloads\\Python Practise\\Youtube_Videos\\saitama_lofi.mp3",
        "key_info": ["e^(iπ) + 1 = 0"],
        "visuals": ["C:\\path_to_images\\euler_formula.png"]
    }
]

if __name__ == "__main__":
    app = VideoPlayer(videos)
    app.mainloop()
