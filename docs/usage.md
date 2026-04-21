# Lorapok Dynamic Ollama LLM Chat Interface - Usage Guide

## Running the Server

1. **Start Ollama**
   ```powershell
   .\scripts\run_server.ps1
   ```

2. **Start Open WebUI** (if installed)
   - If using Docker: The container should start automatically
   - If using pip/source: Run the appropriate command
   - Access at http://localhost:3000 or 8080

## Lorapok Dynamic Console Chat Interface (Like Gemini/Claude)

The enhanced console interface provides a rich, interactive experience similar to Gemini or Claude, powered by the Lorapok Dynamic Ollama LLM Chat Interface.

### Starting the Chat

1. **On Windows (PowerShell)**
   ```powershell
   python src/ollama_client.py
   ```

2. **On Linux/Mac (Terminal)**
   ```bash
   chmod +x chat.sh
   ./chat.sh <server_ip>
   ```
   Or directly:
   ```bash
   python3 src/ollama_client.py <server_ip>
   ```

3. **Cross-platform usage**
   - Works on Windows, macOS, and Linux
   - Requires Python 3.8+ and `requests`, `rich` packages

### Available Commands

| Command | Description |
|---------|-------------|
| `/help` | Show help message with all commands |
| `/model <name>` | Switch to a different model |
| `/models` | List all available models with details |
| `/pull <model>` | Pull a new model from registry |
| `/remove <model>` | Remove an installed model |
| `/history [limit]` | Show conversation history (default: 10) |
| `/search <query>` | Search conversation history |
| `/clear` | Clear conversation history |
| `/save [filename]` | Save conversation to JSON file |
| `/load <filename>` | Load conversation from JSON file |
| `/export <format>` | Export conversation (markdown/text) |
| `/stats` | Show conversation and performance statistics |
| `/bench [model]` | Benchmark current or specified model |
| `/sysinfo` | Show system resource information |
| `/config` | Show current configuration settings |
| `/set <key> <value>` | Update configuration setting |
| `/reset` | Reset configuration to defaults |
| `/exit` | Exit the chat |

### Dynamic Features

The enhanced console interface includes several dynamic features:

#### 🔄 **Dynamic Model Management**
- **Auto-refresh**: Models list updates automatically
- **Smart search**: Find models by partial name matching
- **Pull new models**: Download models directly from the interface
- **Model details**: View size, modification date, and status

#### 💬 **Advanced Conversation Management**
- **Persistent history**: Conversations maintained across sessions
- **Search functionality**: Find specific messages in history
- **Export options**: Save conversations in multiple formats
- **Statistics tracking**: Monitor message counts and performance

#### 📊 **Performance Monitoring**
- **Real-time metrics**: Response times, token counts, throughput
- **Benchmarking**: Test model performance with standard prompts
- **System monitoring**: CPU, memory, and disk usage tracking
- **Historical data**: Performance trends over time

#### ⚙️ **Dynamic Configuration**
- **Runtime settings**: Change configuration without restart
- **Persistent config**: Settings saved to `config.json`
- **Flexible options**: Timeout, streaming, history limits, etc.
- **Reset capability**: Restore default settings

#### 🎨 **Rich Console Experience**
- **Live streaming**: Real-time response updates
- **Colored output**: Syntax highlighting and status indicators
- **Interactive tables**: Formatted data display
- **Progress indicators**: Visual feedback for long operations

### Example Session

```
🤖 Local LLM Chat Interface
Connected to: 192.168.0.219
Current Model: qwen2.5-coder:7b-instruct

Type your message and press Enter.
Commands: /help, /model, /history, /clear, /exit

You: Hello, how are you?
Assistant (qwen2.5-coder:7b-instruct)
Hello! I'm doing well, thank you for asking. How can I help you today?

You: /model llama2:7b
✅ Switched to: llama2:7b

You: Tell me a joke
Assistant (llama2:7b)
Why don't scientists trust atoms? Because they make up everything!
```

## Connecting from Another PC

## Using with VS Code

1. **Install Ollama extension**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Ollama" and install

2. **Configure the extension**
   - Set the Ollama server URL to `http://<server_ip>:11434`
   - Use the chat panel for AI assistance

## API Usage

The Ollama API is available at `http://localhost:11434`

### List Models
```bash
curl http://localhost:11434/api/tags
```

### Generate Response
```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5-coder:7b-instruct", "prompt": "Hello"}'
```

## Managing Models

- **List installed models**: `ollama list`
- **Pull a model**: `ollama pull <model_name>`
- **Remove a model**: `ollama rm <model_name>`

## Available Models

Popular models to try:
- `llama2:7b`
- `codellama:7b`
- `mistral:7b`
- `qwen2.5-coder:7b-instruct` (default)