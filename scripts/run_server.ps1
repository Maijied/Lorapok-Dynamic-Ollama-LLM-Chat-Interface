# Lorapok Dynamic Ollama LLM Chat Interface - Server Runner
# This script starts the Ollama server

Write-Host "Starting Ollama server..." -ForegroundColor Green

# Start Ollama server in background, accessible from network
Start-Job -ScriptBlock {
    ollama serve --host 0.0.0.0
} -Name "OllamaServer"

Write-Host "Ollama server started!" -ForegroundColor Green
Write-Host "API available at: http://localhost:11434" -ForegroundColor Yellow
Write-Host "Accessible from network at: http://<your_ip>:11434" -ForegroundColor Yellow
Write-Host "For Open WebUI, install and run it separately." -ForegroundColor Yellow
Write-Host "See docs/setup.md for Open WebUI installation." -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow

# Wait for user input to keep script running
Read-Host