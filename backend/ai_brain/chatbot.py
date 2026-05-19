import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "phi3"

SYSTEM_PROMPT = """
You are WARHEAD, an intelligent AI assistant.
Give short, fast, direct responses.
Be conversational and concise.
"""

def get_ai_response(user_input):

    prompt = f"""
    {SYSTEM_PROMPT}

    User: {user_input}
    WARHEAD:
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 80
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        data = response.json()

        return data["response"].strip()

    except Exception as e:

        print(e)

        return "AI connection failed"