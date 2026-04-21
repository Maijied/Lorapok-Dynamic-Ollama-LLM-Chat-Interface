# Lorapok Dynamic Ollama LLM Chat Interface - API Documentation

## Ollama API

The Ollama server provides a REST API for interacting with LLMs.

Base URL: `http://localhost:11434`

### Endpoints

#### GET /api/tags
List available models.

**Response:**
```json
{
  "models": [
    {
      "name": "qwen2.5-coder:7b-instruct",
      "size": "4.7GB",
      "modified_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### POST /api/generate
Generate a response from a prompt.

**Request:**
```json
{
  "model": "qwen2.5-coder:7b-instruct",
  "prompt": "Write a hello world program in Python",
  "stream": true
}
```

**Response (streaming):**
```
{"response": "Here", "done": false}
{"response": " is", "done": false}
{"response": " a", "done": false}
...
{"response": "!", "done": true}
```

#### POST /api/chat
Chat with a model (conversational).

**Request:**
```json
{
  "model": "qwen2.5-coder:7b-instruct",
  "messages": [
    {"role": "user", "content": "Hello"}
  ],
  "stream": true
}
```

## Python Client

The included `src/ollama_client.py` provides a Python wrapper for the API in the Lorapok Dynamic Ollama LLM Chat Interface.

### Usage

```python
from src.ollama_client import OllamaClient

client = OllamaClient("192.168.1.100")  # Server IP

# List models
models = client.list_models()
print(models)

# Generate response
response = client.generate("Hello, how are you?")
print(response)

# Interactive chat
client.chat()
```

### Class Methods

- `__init__(server_ip)`: Initialize client with server IP
- `list_models()`: Return list of available models
- `generate(prompt, model, stream)`: Generate response from prompt
- `chat()`: Start interactive chat session

## VS Code Integration

The VS Code Ollama extension provides:

- Code completion
- Chat interface
- Model selection
- Context-aware suggestions

Configure the extension with your server URL for remote access.