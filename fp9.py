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

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
