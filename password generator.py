import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)

        self.generated_password = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.generated_password, state='readonly')
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.generated_password.set("Length should be a positive integer.")
                return

            charset = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(charset) for _ in range(length))
            self.generated_password.set(password)
        except ValueError:
            self.generated_password.set("Invalid input! Please enter a valid integer for the length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
