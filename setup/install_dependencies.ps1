# Lorapok Dynamic Ollama LLM Chat Interface - Dependencies Installer
# This script installs all required dependencies for the Lorapok project

Write-Host "Installing Python dependencies..." -ForegroundColor Green

# Check if Python is installed
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3.8+ first." -ForegroundColor Red
    exit 1
}

# Install Python packages
pip install requests rich psutil

Write-Host "Installing Ollama models..." -ForegroundColor Green

# Pull the default model
ollama pull qwen2.5-coder:7b-instruct

Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "Note: Open WebUI needs to be installed separately." -ForegroundColor Yellow
Write-Host "See docs/setup.md for instructions." -ForegroundColor Yellow
Write-Host "Run .\scripts\run_server.ps1 to start Ollama." -ForegroundColor Yellow