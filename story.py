import tkinter as tk
from PIL import Image, ImageTk
import os

class StoryBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Storybook")
        self.current_page = 0

        # List of pages with text and images
        self.pages = [
            {"text": "Once upon a time in a faraway land, there was a beautiful castle.", "image": "castle.png"},
            {"text": "In the castle, there lived a kind princess who loved to read books.", "image": "princess.png"},
            {"text": "One day, she discovered a hidden library filled with magical books.", "image": "lib.png"},
            {"text": "Among the books, she found a map leading to a hidden treasure.", "image":"treasure.png"},
            {"text": "With courage and determination, she embarked on a thrilling adventure.", "image": "adv.png"},
        ]

        # Display the first page
        self.display_page()

        # Navigation buttons
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def display_page(self):
        # Clear the existing widgets
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        # Display text
        text_label = tk.Label(self.root, text=self.pages[self.current_page]["text"], wraplength=400, font=("Arial", 16))
        text_label.pack(pady=20)

        # Display image
        image_path = self.pages[self.current_page]["image"]
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((400, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.root, image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack(pady=10)
        else:
            error_label = tk.Label(self.root, text="Image not found", fg="red", font=("Arial", 12))
            error_label.pack(pady=10)

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.display_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

# Create the main window
root = tk.Tk()
storybook = StoryBook(root)
root.mainloop()
