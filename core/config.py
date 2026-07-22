from groq import AsyncGroq
from dotenv import load_dotenv
import os

load_dotenv()

cliente_groq = AsyncGroq(
    api_key=os.environ.get("IA_API_KEY")
)