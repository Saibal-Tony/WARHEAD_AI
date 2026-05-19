import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "phi3"

def get_ai_response(user_input, memory_context=""):

    prompt = f"""
    You are TONY, an intelligent AI assistant.

    Previous Memory:
    {memory_context}

    User: {user_input}

    TONY:
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

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    data = response.json()

    if "response" in data:

        return data["response"].strip()

    else:

        print("Ollama Error:", data)
        return "I encountered an AI processing error."