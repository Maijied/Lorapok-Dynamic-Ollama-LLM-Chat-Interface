# Lorapok Dynamic Ollama LLM Chat Interface - Setup Guide

## Prerequisites

- Windows 10/11
- Python 3.8+
- Internet connection for downloading models
- Docker (optional, for Open WebUI)

## Installation

1. **Clone or download this project**

2. **Run the installation script**
   ```powershell
   .\setup\install_dependencies.ps1
   ```
   This will:
   - Install required Python packages (requests)
   - Pull the default LLM model (qwen2.5-coder:7b-instruct)

## Open WebUI Installation

Open WebUI provides a web interface for Ollama.

### Option 1: Using Docker (Recommended)
```powershell
# Install Docker Desktop if not already installed
# Then run:
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Option 2: Using pip (Advanced)
```powershell
pip install open-webui
open-webui serve
```

### Option 3: From Source
```powershell
git clone https://github.com/open-webui/open-webui.git
cd open-webui
pip install -r requirements.txt
bash start.sh
```

After installation, access Open WebUI at http://localhost:3000 (or 8080 depending on method).

## Network Configuration

To allow connections from other PCs:

1. **Firewall Settings**
   - Allow inbound connections on port 11434 (Ollama API)
   - Allow inbound connections on port 3000/8080 (Open WebUI)

2. **Find your IP address**
   ```powershell
   ipconfig
   ```
   Look for your local IP (e.g., 192.168.1.100)

## Internet Access (Router Hosting)

⚠️ **Security Warning**: Exposing your LLM server to the internet carries security risks. Ensure you have strong authentication and consider using VPN or API keys.

To access your Ollama server from anywhere on the internet:

### TP-Link Archer C6 Port Forwarding

1. **Access Router Admin Panel**
   - Open browser and go to `http://tplinkwifi.net` or `192.168.0.1`
   - Login with your router credentials (default: admin/admin)

2. **Navigate to Port Forwarding**
   - Go to **Advanced** > **NAT Forwarding** > **Port Forwarding**

3. **Add Port Forwarding Rules**
   - Click **Add**
   - **Name**: Ollama API
   - **External Port**: 11434
   - **Internal IP**: Your PC's local IP (from ipconfig)
   - **Internal Port**: 11434
   - **Protocol**: TCP
   - Click **Save**

4. **For Open WebUI (Optional)**
   - Add another rule:
   - **Name**: Open WebUI
   - **External Port**: 3000 (or your chosen external port)
   - **Internal IP**: Your PC's local IP
   - **Internal Port**: 3000 (or 8080 depending on setup)
   - **Protocol**: TCP

5. **Find Your Public IP**
   - Visit `https://whatismyipaddress.com` or similar
   - Your public IP will be shown

6. **Access from Internet**
   - Ollama API: `http://<your_public_ip>:11434`
   - Open WebUI: `http://<your_public_ip>:3000`

### Additional Setup

- **Dynamic DNS**: If your public IP changes, use a DDNS service like No-IP
- **Firewall**: Ensure Windows Firewall allows the ports
- **Static Local IP**: Set your PC to use a static IP in router settings to prevent IP changes

## VS Code Integration

1. Install the "Ollama" extension from VS Code marketplace
2. Configure the extension to point to your local Ollama server
3. Use the extension for code completion and chat features

## Troubleshooting

- **Cannot connect from another PC**: Check firewall settings and IP address
- **Model not found**: Run `ollama pull <model_name>`
- **Open WebUI not loading**: Ensure the correct port is used and not blocked