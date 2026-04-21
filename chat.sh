#!/bin/bash

# Lorapok Dynamic Ollama LLM Chat Interface Launcher for Linux/macOS
# Usage: ./chat.sh [server_ip]

DEFAULT_IP="192.168.0.219"
SERVER_IP=${1:-$DEFAULT_IP}

echo "🚀 Starting Ollama Chat Client..."
echo "🔗 Connecting to: $SERVER_IP"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if required packages are installed
python3 -c "import requests, rich" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing required packages..."
    pip3 install requests rich
fi

# Run the client
python3 src/ollama_client.py "$SERVER_IP"