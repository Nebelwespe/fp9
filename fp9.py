import tkinter as tk
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path


dotenv_path = Path(__file__).resolve().parent / ".env" #forces it to check for .env files
print("Does .env exist?", os.path.exists(dotenv_path)) #does the env file exist?
load_dotenv(dotenv_path=dotenv_path, override=True)
apikey = os.getenv("OPENAI_API_KEY")


if apikey:
    print("API Key found:", apikey[:8] + "...")
else:
    print("API Key NOT FOUND.") #can it read it?

client = OpenAI(api_key=apikey)





def get_response():
    prompt = prompt_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Enter a prompt first.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
    except Exception as e:
        result = f"Error: {e}"

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# GUI
root = tk.Tk()
root.title("Simple GPT GUI")

prompt_box = tk.Text(root, height=5, width=60)
prompt_box.pack(padx=10, pady=5)

submit_btn = tk.Button(root, text="Submit", command=get_response)
submit_btn.pack(pady=5)

output_box = tk.Text(root, height=10, width=60)
output_box.pack(padx=10, pady=5)

root.mainloop()

