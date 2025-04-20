import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).resolve().parent / ".env"  #forces it to load .env files
print("Does .env exist?", os.path.exists(dotenv_path))  #forces it to check for .env files

load_dotenv(dotenv_path=dotenv_path, override=True)
apikey = os.getenv("OPENAI_API_KEY")

if apikey:
    print("API Key found:", apikey) #checks to make sure it's loaded the API key correctly
else:
    print("API Key NOT FOUND.")
    raise ValueError("API Key not found in .env file.")

client = OpenAI(api_key=apikey)

def create_gui():
    def submit_prompt():
        prompt = prompt_input.get("1.0", tk.END).strip()
        if not prompt:
            messagebox.showwarning("Input Error", "Please enter a prompt.")
            return

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
        except Exception as e:
            output = f"Error: {e}"

        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state='disabled')

    root = tk.Tk()
    root.title("ChatGPT Prompt GUI")
    root.geometry("600x500")

    ttk.Label(root, text="Enter your prompt below:", font=("Arial", 12)).pack(pady=10)

    prompt_input = scrolledtext.ScrolledText(root, height=6, wrap=tk.WORD)
    prompt_input.pack(padx=10, fill=tk.BOTH)

    ttk.Button(root, text="Submit", command=submit_prompt).pack(pady=10)

    ttk.Label(root, text="Response:", font=("Arial", 12)).pack(pady=5)

    output_box = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD, state='disabled')
    output_box.pack(padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()

create_gui()
