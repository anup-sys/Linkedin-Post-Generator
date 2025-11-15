import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def generate_post(topic, tone, audience, points):
    """
    Generate a clean, polished, professional LinkedIn post using Gemini 2.5 Flash.
    """

    prompt = f"""
You are an expert LinkedIn content writer.

Write a professional LinkedIn post based on the following:

Topic: {topic}
Tone: {tone}
Audience: {audience}
Bullet Points: {points}

STRICT REQUIREMENTS:
- Use a clean, crisp, easy-to-read style.
- Include storytelling or insights when appropriate.
- Keep the flow smooth and professional.
- Do NOT use emojis unless necessary.
- Add 4–6 relevant, trending hashtags at the end.
- Make it engaging and high-value for LinkedIn readers.

Return ONLY the post text.
"""

    # Recommended model for your account (FAST + QUALITY)
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text

