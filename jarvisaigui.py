import tkinter as tk
from tkinter import scrolledtext, messagebox
from Jarvisaicore import JarvisCore

class JarvisBotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jarvis - Your Super Bot")
        self.jarvis_core = JarvisCore()

        # Create and configure the text box
        self.text_box = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=15)
        self.text_box.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Create Entry for user input
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.master, textvariable=self.entry_var, width=40)
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        # Create the 'Ask Jarvis' button
        ask_button = tk.Button(self.master, text="Ask Jarvis", command=self.ask_jarvis)
        ask_button.grid(row=1, column=1, pady=10)

        # Create the 'Clear' button
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_text_box)
        clear_button.grid(row=1, column=2, pady=10)

    def ask_jarvis(self):
        # Get user input from the Entry widget
        user_input = self.entry_var.get().strip()

        if user_input:
            # Display user input in the text box
            self.text_box.insert(tk.END, f"You: {user_input}\n")

            try:
                # Process user input using Jarvis Core
                response = self.jarvis_core.respond(user_input)
            except Exception as e:
                # Handle any errors from JarvisCore
                response = f"Error: {str(e)}"

            # Display Jarvis response in the text box
            self.text_box.insert(tk.END, f"Jarvis: {response}\n")

            # Clear the Entry widget
            self.entry_var.set("")
        else:
            messagebox.showwarning("Empty Input", "Please enter a question or command.")

    def clear_text_box(self):
        # Clear the entire text box
        self.text_box.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    jarvis_bot_gui = JarvisBotGUI(root)
    root.mainloop()
