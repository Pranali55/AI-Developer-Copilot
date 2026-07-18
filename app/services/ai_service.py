import os

from openai import OpenAI

from app.config import OPENROUTER_API_KEY
from app.config import MODEL_NAME


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(system_prompt: str, user_prompt: str) -> str:
    """
    Generic AI request function.
    """

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0.3,
            max_tokens=2048

        )

        return response.choices[0].message.content.strip()

    except Exception as e:

        return f"AI Error: {str(e)}"


def explain_code(code: str, prompt: str):

    return ask_ai(prompt, code)


def review_code(code: str, prompt: str):

    return ask_ai(prompt, code)


def security_review(code: str, prompt: str):

    return ask_ai(prompt, code)


def performance_review(code: str, prompt: str):

    return ask_ai(prompt, code)


def generate_documentation(code: str, prompt: str):

    return ask_ai(prompt, code)


def generate_unit_tests(code: str, prompt: str):

    return ask_ai(prompt, code)


def convert_code(code: str, prompt: str):

    return ask_ai(prompt, code)


def chat_with_code(code: str, question: str):

    prompt = f"""
Source Code

{code}

User Question

{question}

Answer clearly and professionally.
"""

    return ask_ai(
        "You are an expert software engineer.",
        prompt
    )
def generate_unit_tests(code: str, prompt: str):
    """
    Generate unit tests for the given source code.
    """
    return ask_ai(prompt, code)
def convert_code(code: str, prompt: str):
    """
    Convert source code into another programming language.
    """
    return ask_ai(prompt, code)