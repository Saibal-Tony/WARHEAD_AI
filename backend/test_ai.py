import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3",
        "prompt": "Tell me a joke",
        "stream": False
    }
)

print(response.json()["response"])