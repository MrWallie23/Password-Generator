import tkinter as tk
import random
import string

def main():
    def generate_random_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    app = tk.Tk()
    app.title("Random Password Generator")
    app.geometry("300x150")

    password_label = tk.Label(app, text="CodeSlayers Random Password:")
    password_label.pack(pady=10)

    password_entry = tk.Entry(app, width=30)
    password_entry.pack(pady=5)

    generate_button = tk.Button(app, text="Generate Password", command=generate_random_password)
    generate_button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()