# Lorapok Dynamic Ollama LLM Chat Interface - Client Launcher
# Run this on client PCs to connect to the server

param(
    [string]$ServerIP = "192.168.0.219"
)

Write-Host "Connecting to Ollama server at $ServerIP..." -ForegroundColor Green

python "src/ollama_client.py" $ServerIP