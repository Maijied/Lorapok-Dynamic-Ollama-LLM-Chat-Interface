"""
Lorapok Dynamic Ollama LLM Chat Interface

A comprehensive, dynamic console-based interface for interacting with Ollama LLMs.
Features include real-time performance monitoring, advanced conversation management,
dynamic model switching, and cross-platform compatibility.

Author: GitHub Copilot
Version: 1.0.0
"""

class OllamaClient:
    def __init__(self, server_ip: str = None):
        # Load dynamic configuration
        self.config_manager = DynamicConfig()
        self.config = self.config_manager.get_config()

        # Use provided server_ip or config default
        self.server_ip = server_ip or self.config.server_ip
        self.base_url = f"http://{self.server_ip}:11434"

        # Initialize console
        self.console = Console()

        # Initialize dynamic managers
        self.model_manager = DynamicModelManager(self.base_url, self.console)
        self.conversation_manager = DynamicConversationManager(self.console, self.config.max_history)
        self.performance_monitor = DynamicPerformanceMonitor(self.base_url, self.console)

        # Current model
        self.current_model = self.config.default_model

    def list_models(self):
        """Show available models"""
        try:
            r = requests.get(f"{self.base_url}/api/tags", timeout=5)
            models = r.json().get("models", [])
            return [m["name"] for m in models]
        except Exception as e:
            return f"Error: {e}"

    def generate(self, prompt, model=None, stream=None):
        """Generate response from prompt with dynamic features"""
        if model is None:
            model = self.current_model
        if stream is None:
            stream = self.config.stream_responses

        start_time = time.time()

        try:
            r = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": stream
                },
                stream=stream,
                timeout=self.config.timeout
            )
            r.raise_for_status()

            full_response = ""
            if stream:
                with Live(console=self.console, refresh_per_second=10) as live:
                    for line in r.iter_lines():
                        if line:
                            data = json.loads(line)
                            if "response" in data:
                                chunk = data["response"]
                                full_response += chunk
                                live.update(Text(full_response, style="bold green"))
                    live.update(Text(full_response, style="bold green"))
            else:
                data = r.json()
                full_response = data["response"]
                self.console.print(Text(full_response, style="bold green"))

            # Calculate performance metrics
            end_time = time.time()
            response_time = end_time - start_time
            tokens_generated = len(full_response.split()) * 1.3  # Rough estimation

            # Add to conversation history
            self.conversation_manager.add_message("user", prompt, model)
            self.conversation_manager.add_message("assistant", full_response, model,
                                                tokens=int(tokens_generated), response_time=response_time)

            return full_response

        except Exception as e:
            self.console.print(f"[red]❌ Error: {e}[/red]")
            return None

    def show_welcome(self):
        """Display welcome screen with dynamic info"""
        # Get current models
        models = self.model_manager.get_model_names()
        model_count = len(models)

        # Get conversation stats
        stats = self.conversation_manager.get_conversation_stats()

        welcome_text = f"""
[bold blue]🤖 Lorapok Dynamic Ollama LLM Chat Interface[/bold blue]
[cyan]Connected to:[/cyan] {self.server_ip}
[cyan]Current Model:[/cyan] {self.current_model}
[cyan]Available Models:[/cyan] {model_count}
[cyan]Conversation Messages:[/cyan] {stats['total_messages']}

[dim]Commands: /help, /model, /models, /history, /clear, /save, /load, /stats, /bench, /config, /exit[/dim]
        """
        self.console.print(Panel(welcome_text, title="Welcome", border_style="blue"))

    def show_help(self):
        """Show help information with all dynamic commands"""
        help_table = Table(title="Available Commands")
        help_table.add_column("Command", style="cyan", no_wrap=True)
        help_table.add_column("Description", style="magenta")

        commands = [
            ("/help", "Show this help message"),
            ("/model <name>", "Switch to a different model"),
            ("/models", "List all available models with details"),
            ("/pull <model>", "Pull a new model from registry"),
            ("/remove <model>", "Remove a model"),
            ("/history [limit]", "Show conversation history"),
            ("/search <query>", "Search conversation history"),
            ("/clear", "Clear conversation history"),
            ("/save [filename]", "Save conversation to JSON file"),
            ("/load <filename>", "Load conversation from JSON file"),
            ("/export <format>", "Export conversation (markdown/text)"),
            ("/stats", "Show conversation and performance statistics"),
            ("/bench [model]", "Benchmark current or specified model"),
            ("/sysinfo", "Show system information"),
            ("/config", "Show current configuration"),
            ("/set <key> <value>", "Update configuration setting"),
            ("/reset", "Reset configuration to defaults"),
            ("/exit", "Exit the chat")
        ]

        for cmd, desc in commands:
            help_table.add_row(cmd, desc)

        self.console.print(help_table)

    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            self.console.print("[yellow]No conversation history yet.[/yellow]")
            return

        history_table = Table(title="Conversation History")
        history_table.add_column("Time", style="dim", width=12)
        history_table.add_column("Role", style="bold", width=6)
        history_table.add_column("Message", style="white")

        for entry in self.conversation_history[-10:]:  # Show last 10
            time_str = entry['time'].strftime("%H:%M:%S")
            role = "You" if entry['role'] == 'user' else "AI"
            message = entry['message'][:100] + "..." if len(entry['message']) > 100 else entry['message']
            history_table.add_row(time_str, role, message)

        self.console.print(history_table)

    def save_conversation(self):
        """Save conversation to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"

        try:
            with open(filename, 'w') as f:
                json.dump(self.conversation_history, f, default=str, indent=2)
            self.console.print(f"[green]✅ Conversation saved to {filename}[/green]")
        except Exception as e:
            self.console.print(f"[red]❌ Failed to save: {e}[/red]")

    def chat(self):
        """Interactive chat mode with dynamic features"""
        self.show_welcome()

        while True:
            try:
                # Get user input with rich prompt
                user_input = Prompt.ask("[bold cyan]You[/bold cyan]").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.lower() in ['exit', 'quit', 'q', '/exit']:
                    self.console.print("[yellow]👋 Goodbye![/yellow]")
                    break

                elif user_input.lower() in ['help', '/help']:
                    self.show_help()
                    continue

                elif user_input.lower() == '/models':
                    self.model_manager.show_models_table(self.current_model)
                    continue

                elif user_input.startswith('/model '):
                    new_model = user_input.split(' ', 1)[1]
                    model_info = self.model_manager.find_model(new_model)
                    if model_info:
                        self.current_model = model_info.name
                        self.console.print(f"[green]✅ Switched to: {model_info.name}[/green]")
                    else:
                        self.console.print(f"[red]❌ Model '{new_model}' not found[/red]")
                    continue

                elif user_input.startswith('/pull '):
                    model_name = user_input.split(' ', 1)[1]
                    self.model_manager.pull_model(model_name)
                    continue

                elif user_input.startswith('/remove '):
                    model_name = user_input.split(' ', 1)[1]
                    self.model_manager.remove_model(model_name)
                    continue

                elif user_input.startswith('/history'):
                    parts = user_input.split()
                    limit = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 10
                    self.conversation_manager.show_history(limit)
                    continue

                elif user_input.startswith('/search '):
                    query = user_input.split(' ', 1)[1]
                    results = self.conversation_manager.search_messages(query)
                    if results:
                        search_table = Table(title=f"Search Results for '{query}'")
                        search_table.add_column("Time", style="dim", width=12)
                        search_table.add_column("Role", style="bold", width=6)
                        search_table.add_column("Match", style="white")

                        for msg in results[-10:]:  # Show last 10 matches
                            time_str = msg.timestamp.strftime("%H:%M:%S")
                            role = "You" if msg.role == "user" else "AI"
                            # Highlight the query in the message
                            content = msg.content
                            if len(content) > 100:
                                # Find context around the query
                                query_lower = query.lower()
                                idx = content.lower().find(query_lower)
                                if idx >= 0:
                                    start = max(0, idx - 50)
                                    end = min(len(content), idx + len(query) + 50)
                                    content = "..." + content[start:end] + "..."
                            search_table.add_row(time_str, role, content)
                        self.console.print(search_table)
                    else:
                        self.console.print(f"[yellow]No messages found containing '{query}'[/yellow]")
                    continue

                elif user_input.lower() == '/clear':
                    self.conversation_manager.clear_history()
                    self.console.print("[green]✅ Conversation history cleared[/green]")
                    continue

                elif user_input.startswith('/save'):
                    parts = user_input.split()
                    filename = parts[1] if len(parts) > 1 else None
                    self.conversation_manager.save_conversation(filename)
                    continue

                elif user_input.startswith('/load '):
                    filename = user_input.split(' ', 1)[1]
                    self.conversation_manager.load_conversation(filename)
                    continue

                elif user_input.startswith('/export '):
                    format_type = user_input.split(' ', 1)[1]
                    exported = self.conversation_manager.export_conversation(format_type)
                    # Save to file
                    ext = "md" if format_type.lower() == "markdown" else "txt"
                    filename = f"conversation_export.{ext}"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(exported)
                    self.console.print(f"[green]✅ Conversation exported to {filename}[/green]")
                    continue

                elif user_input.lower() == '/stats':
                    # Show conversation stats
                    conv_stats = self.conversation_manager.get_conversation_stats()
                    stats_table = Table(title="Conversation Statistics")
                    stats_table.add_column("Metric", style="cyan")
                    stats_table.add_column("Value", style="green")

                    stats_table.add_row("Total Messages", str(conv_stats["total_messages"]))
                    stats_table.add_row("User Messages", str(conv_stats["user_messages"]))
                    stats_table.add_row("Assistant Messages", str(conv_stats["assistant_messages"]))
                    stats_table.add_row("Total Tokens", str(conv_stats["total_tokens"]))
                    stats_table.add_row("Avg Response Time", f"{conv_stats['avg_response_time']}s")

                    self.console.print(stats_table)

                    # Show performance stats
                    self.performance_monitor.show_performance_stats()
                    continue

                elif user_input.startswith('/bench'):
                    parts = user_input.split()
                    model = parts[1] if len(parts) > 1 else self.current_model
                    self.performance_monitor.benchmark_model(model)
                    continue

                elif user_input.lower() == '/sysinfo':
                    self.performance_monitor.show_system_stats()
                    continue

                elif user_input.lower() == '/config':
                    config_table = Table(title="Current Configuration")
                    config_table.add_column("Setting", style="cyan")
                    config_table.add_column("Value", style="green")

                    config_dict = {
                        "Server IP": self.config.server_ip,
                        "Default Model": self.config.default_model,
                        "Max History": self.config.max_history,
                        "Auto Save": self.config.auto_save,
                        "Theme": self.config.theme,
                        "Show Timestamps": self.config.show_timestamps,
                        "Stream Responses": self.config.stream_responses,
                        "Timeout": self.config.timeout,
                        "Max Retries": self.config.max_retries
                    }

                    for key, value in config_dict.items():
                        config_table.add_row(key, str(value))

                    self.console.print(config_table)
                    continue

                elif user_input.startswith('/set '):
                    parts = user_input.split()
                    if len(parts) >= 3:
                        key, value = parts[1], ' '.join(parts[2:])
                        # Try to convert value to appropriate type
                        if value.isdigit():
                            value = int(value)
                        elif value.lower() in ['true', 'false']:
                            value = value.lower() == 'true'

                        if self.config_manager.update_config(key, value):
                            self.console.print(f"[green]✅ Updated {key} = {value}[/green]")
                            # Reload config
                            self.config = self.config_manager.get_config()
                        else:
                            self.console.print(f"[red]❌ Invalid setting: {key}[/red]")
                    else:
                        self.console.print("[red]Usage: /set <key> <value>[/red]")
                    continue

                elif user_input.lower() == '/reset':
                    self.config_manager.reset_to_defaults()
                    self.config = self.config_manager.get_config()
                    self.console.print("[green]✅ Configuration reset to defaults[/green]")
                    continue

                # Regular chat message
                # Show AI response header
                self.console.print(f"[bold green]Assistant[/bold green] [dim]({self.current_model})[/dim]")

                # Generate response
                response = self.generate(user_input, model=self.current_model)

            except KeyboardInterrupt:
                self.console.print("\n[yellow]👋 Interrupted. Goodbye![/yellow]")
                break
            except EOFError:
                break

if __name__ == "__main__":
    # Default to your server IP
    server_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.0.219"

    console = Console()
    console.print(f"[blue]� Starting Lorapok Dynamic Ollama LLM Chat Interface...[/blue]")
    console.print(f"[blue]🔗 Connecting to {server_ip}...[/blue]")

    client = OllamaClient(server_ip)

    # Test connection
    try:
        requests.get(f"http://{server_ip}:11434", timeout=5)
        client.chat()
    except Exception as e:
        console.print(f"\n[red]❌ Cannot connect to {server_ip}:11434[/red]")
        console.print(f"[red]   Error: {e}[/red]")
        console.print(f"\n[cyan]💡 Make sure:[/cyan]")
        console.print(f"   1. Server PC ({server_ip}) is running Lorapok/Ollama")
        console.print(f"   2. Ollama is running on server")
        console.print(f"   3. Both PCs are on same network")
