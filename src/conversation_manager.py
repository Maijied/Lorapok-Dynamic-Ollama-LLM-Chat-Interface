import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

@dataclass
class Message:
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: datetime
    model: str = ""
    tokens: int = 0
    response_time: float = 0.0

class DynamicConversationManager:
    def __init__(self, console: Console, max_history: int = 100):
        self.console = console
        self.messages: List[Message] = []
        self.max_history = max_history
        self.current_conversation_file = None

    def add_message(self, role: str, content: str, model: str = "", tokens: int = 0, response_time: float = 0.0):
        """Add a message to the conversation"""
        message = Message(
            role=role,
            content=content,
            timestamp=datetime.now(),
            model=model,
            tokens=tokens,
            response_time=response_time
        )

        self.messages.append(message)

        # Trim history if too long
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]

    def get_messages(self, limit: Optional[int] = None) -> List[Message]:
        """Get messages, optionally limited"""
        if limit:
            return self.messages[-limit:]
        return self.messages

    def clear_history(self):
        """Clear all messages"""
        self.messages.clear()
        self.current_conversation_file = None

    def search_messages(self, query: str) -> List[Message]:
        """Search messages containing the query"""
        query_lower = query.lower()
        return [msg for msg in self.messages
                if query_lower in msg.content.lower()]

    def get_conversation_stats(self) -> Dict:
        """Get conversation statistics"""
        if not self.messages:
            return {"total_messages": 0, "user_messages": 0, "assistant_messages": 0,
                   "total_tokens": 0, "avg_response_time": 0}

        user_msgs = [msg for msg in self.messages if msg.role == "user"]
        assistant_msgs = [msg for msg in self.messages if msg.role == "assistant"]

        total_tokens = sum(msg.tokens for msg in self.messages)
        total_response_time = sum(msg.response_time for msg in assistant_msgs)
        avg_response_time = total_response_time / len(assistant_msgs) if assistant_msgs else 0

        return {
            "total_messages": len(self.messages),
            "user_messages": len(user_msgs),
            "assistant_messages": len(assistant_msgs),
            "total_tokens": total_tokens,
            "avg_response_time": round(avg_response_time, 2)
        }

    def show_history(self, limit: int = 10):
        """Display conversation history"""
        messages = self.get_messages(limit)

        if not messages:
            self.console.print("[yellow]No conversation history[/yellow]")
            return

        table = Table(title=f"Conversation History (Last {len(messages)} messages)")
        table.add_column("Time", style="dim", width=12)
        table.add_column("Role", style="bold", width=8)
        table.add_column("Model", style="cyan", width=15)
        table.add_column("Message", style="white")
        table.add_column("Tokens", style="green", width=6)
        table.add_column("Time", style="yellow", width=6)

        for msg in messages:
            time_str = msg.timestamp.strftime("%H:%M:%S")
            role_display = "You" if msg.role == "user" else "AI"
            model_display = msg.model[:14] + "..." if len(msg.model) > 14 else msg.model
            content_preview = msg.content[:50] + "..." if len(msg.content) > 50 else msg.content
            tokens_display = str(msg.tokens) if msg.tokens > 0 else ""
            time_display = f"{msg.response_time:.1f}s" if msg.response_time > 0 else ""

            table.add_row(time_str, role_display, model_display, content_preview,
                         tokens_display, time_display)

        self.console.print(table)

    def save_conversation(self, filename: Optional[str] = None) -> bool:
        """Save conversation to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"

        try:
            # Convert messages to dicts
            data = {
                "metadata": {
                    "saved_at": datetime.now().isoformat(),
                    "total_messages": len(self.messages),
                    "stats": self.get_conversation_stats()
                },
                "messages": [
                    {
                        "role": msg.role,
                        "content": msg.content,
                        "timestamp": msg.timestamp.isoformat(),
                        "model": msg.model,
                        "tokens": msg.tokens,
                        "response_time": msg.response_time
                    }
                    for msg in self.messages
                ]
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            self.current_conversation_file = filename
            self.console.print(f"[green]✅ Conversation saved to {filename}[/green]")
            return True

        except Exception as e:
            self.console.print(f"[red]❌ Failed to save conversation: {e}[/red]")
            return False

    def load_conversation(self, filename: str) -> bool:
        """Load conversation from JSON file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.messages.clear()
            for msg_data in data.get("messages", []):
                message = Message(
                    role=msg_data["role"],
                    content=msg_data["content"],
                    timestamp=datetime.fromisoformat(msg_data["timestamp"]),
                    model=msg_data.get("model", ""),
                    tokens=msg_data.get("tokens", 0),
                    response_time=msg_data.get("response_time", 0.0)
                )
                self.messages.append(message)

            self.current_conversation_file = filename
            self.console.print(f"[green]✅ Loaded conversation from {filename}[/green]")
            return True

        except Exception as e:
            self.console.print(f"[red]❌ Failed to load conversation: {e}[/red]")
            return False

    def export_conversation(self, format: str = "markdown") -> str:
        """Export conversation in different formats"""
        if format.lower() == "markdown":
            lines = [f"# Conversation Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
            for msg in self.messages:
                role_display = "👤 **You**" if msg.role == "user" else f"🤖 **Assistant** ({msg.model})"
                timestamp = msg.timestamp.strftime("%H:%M:%S")
                lines.append(f"### {role_display} - {timestamp}")
                lines.append(f"{msg.content}\n")
            return "\n".join(lines)

        elif format.lower() == "text":
            lines = [f"Conversation Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
            for msg in self.messages:
                role_display = "You:" if msg.role == "user" else f"Assistant ({msg.model}):"
                lines.append(f"[{msg.timestamp.strftime('%H:%M:%S')}] {role_display}")
                lines.append(f"{msg.content}\n")
            return "\n".join(lines)

        return "Unsupported format"