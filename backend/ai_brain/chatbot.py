import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "phi3"

def get_ai_response(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        data = response.json()

        return data["response"]

    except Exception as e:
        print(e)

        return "AI brain connection failed"