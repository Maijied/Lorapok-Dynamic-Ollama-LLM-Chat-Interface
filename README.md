# Lorapok Dynamic Ollama LLM Chat Interface

This project provides a complete setup for running Large Language Models (LLMs) locally using Ollama, with a **dynamic console interface** similar to Gemini/Claude, web UI access via Open WebUI, VS Code integration, and API server capabilities. It supports connecting from other PCs on the network and works across Windows, macOS, and Linux.

## Features

- ✅ Run local LLM using Ollama
- ✅ **Dynamic console chat interface** (like Gemini/Claude)
- ✅ **Real-time performance monitoring** and benchmarking
- ✅ **Advanced conversation management** with search and export
- ✅ **Dynamic model management** with auto-refresh
- ✅ **Configurable settings** with persistent storage
- ✅ Connect from another PC on the network
- ✅ Access from anywhere via internet (router port forwarding)
- ✅ Use Open WebUI for web-based interface
- ✅ Integrate with VS Code
- ✅ Run API server for programmatic access
- ✅ Cross-platform support (Windows/Mac/Linux)

## 🌐 Website & Documentation

Visit our [professional website](https://maijied.github.io/Lorapok-Dynamic-Ollama-LLM-Chat-Interface) for:
- 📖 Complete documentation and guides
- 🎯 Interactive feature demonstrations
- 📋 Installation instructions for all platforms
- 🔧 API reference and integration examples
- 📊 Performance benchmarks and comparisons
- 💻 Code examples and usage patterns

The website includes a live terminal demo, download links, and comprehensive guides to get you started quickly.

## 🚀 Quick Start

1. **Install Dependencies**
   ```powershell
   .\setup\install_dependencies.ps1
   ```

2. **Pull a Model**
   ```powershell
   ollama pull qwen2.5-coder:7b-instruct
   ```

3. **Run the Server**
   ```powershell
   .\scripts\run_server.ps1
   ```

4. **Access Open WebUI**
   Open http://localhost:8080 in your browser

5. **Start Dynamic Console Chat**
   ```powershell
   python src/ollama_client.py
   ```
   Try commands like `/help`, `/models`, `/stats`, `/bench`

6. **Connect from Another PC**
   Use the client script: `python src/ollama_client.py <server_ip>`

7. **Internet Access (Optional)**
   Configure port forwarding on your router for remote access. See [docs/setup.md](docs/setup.md) for TP-Link Archer C6 instructions.

## 🎯 Key Dynamic Features

### 🤖 **Advanced Model Management**
- **Auto-discovery**: Automatically detects and refreshes available models
- **Smart switching**: Switch models with partial name matching
- **Pull & remove**: Download or remove models directly from chat
- **Performance tracking**: Monitor response times and token usage

### 💬 **Intelligent Conversation System**
- **Persistent history**: Conversations saved across sessions
- **Advanced search**: Find messages by content
- **Multiple export formats**: Save as JSON, Markdown, or plain text
- **Statistics dashboard**: Track conversation metrics

### 📊 **Real-time Performance Monitoring**
- **Live benchmarking**: Test model performance with standard prompts
- **System monitoring**: CPU, memory, and disk usage tracking
- **Response analytics**: Average times, token counts, throughput
- **Historical trends**: Performance data over time

### ⚙️ **Dynamic Configuration**
- **Runtime settings**: Change config without restarting
- **Persistent storage**: Settings saved to `config.json`
- **Flexible options**: Customize timeouts, streaming, history limits
- **Easy reset**: Restore defaults anytime

### 🎨 **Rich Interactive Experience**
- **Live streaming**: Real-time response generation
- **Colored interface**: Syntax highlighting and status indicators
- **Interactive tables**: Formatted data display
- **Progress feedback**: Visual indicators for operations

## Project Structure

```
├── setup/              # Installation scripts
├── scripts/            # Runtime scripts
├── src/                # Source code
│   ├── ollama_client.py    # Main dynamic chat client
│   ├── config.py          # Dynamic configuration system
│   ├── model_manager.py   # Model management utilities
│   ├── conversation_manager.py  # Conversation handling
│   └── performance_monitor.py   # Performance tracking
├── docs/               # Documentation
│   └── website/         # GitHub Pages website
│       ├── index.html   # Main website
│       ├── styles.css   # Professional styling
│       ├── script.js    # Interactive features
│       └── README.md    # Website documentation
├── .github/            # GitHub Actions workflows
│   └── workflows/       # CI/CD automation
├── config.json         # Configuration file
└── README.md          # This file
```

## Detailed Setup

See [docs/setup.md](docs/setup.md) for detailed installation instructions.

## Usage

See [docs/usage.md](docs/usage.md) for usage examples.

## API Documentation

See [docs/api.md](docs/api.md) for API reference.