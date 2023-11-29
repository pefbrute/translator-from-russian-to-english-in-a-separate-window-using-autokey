import pyperclip
import pyautogui
import time
from googletrans import Translator
import tkinter as tk

translator = Translator()

def translate_to_english():
    pyautogui.hotkey('ctrl', 'c')  # Use 'command' instead of 'ctrl' on macOS
    
    time.sleep(0.1)  # Wait a bit for the clipboard to update with the selected text
    
    # Get the text from the clipboard
    input_text = pyperclip.paste()
    
    translated = translator.translate(input_text, dest='ru').text
    
    pyperclip.copy(translated)

    # Update the GUI window with the translated text
    update_gui(translated)

def create_gui():
    window = tk.Tk()
    window.title("Translation")
    window.geometry("400x200")

    global translation_label
    translation_label = tk.Label(window, text="", wraplength=380, anchor='w', justify='left')
    translation_label.pack(expand=True, fill='both')

    return window

def update_gui(translated_text):
    translation_label.config(text=translated_text)

# Create the GUI window
gui_window = create_gui()

# Trigger the translation and GUI update
translate_to_english()

# Start the GUI event loop
gui_window.mainloop()
