import requests
import time
from typing import List, Dict, Optional
from dataclasses import dataclass
from rich.table import Table
from rich.console import Console

@dataclass
class ModelInfo:
    name: str
    size: str
    modified_at: str
    digest: str = ""
    details: Dict = None

class DynamicModelManager:
    def __init__(self, base_url: str, console: Console):
        self.base_url = base_url
        self.console = console
        self.models_cache: List[ModelInfo] = []
        self.last_refresh = 0
        self.cache_timeout = 30  # seconds

    def refresh_models(self, force: bool = False) -> List[ModelInfo]:
        """Refresh the models list with caching"""
        current_time = time.time()
        if not force and current_time - self.last_refresh < self.cache_timeout:
            return self.models_cache

        try:
            r = requests.get(f"{self.base_url}/api/tags", timeout=5)
            r.raise_for_status()
            data = r.json()

            self.models_cache = []
            for model_data in data.get("models", []):
                model = ModelInfo(
                    name=model_data["name"],
                    size=model_data.get("size", "Unknown"),
                    modified_at=model_data.get("modified_at", "Unknown"),
                    digest=model_data.get("digest", ""),
                    details=model_data.get("details", {})
                )
                self.models_cache.append(model)

            self.last_refresh = current_time
            return self.models_cache

        except Exception as e:
            self.console.print(f"[red]Error refreshing models: {e}[/red]")
            return self.models_cache

    def get_models(self) -> List[ModelInfo]:
        """Get current models list"""
        return self.refresh_models()

    def get_model_names(self) -> List[str]:
        """Get just the model names"""
        return [model.name for model in self.get_models()]

    def find_model(self, name: str) -> Optional[ModelInfo]:
        """Find a model by name (partial match)"""
        models = self.get_models()
        # Exact match first
        for model in models:
            if model.name == name:
                return model
        # Partial match
        for model in models:
            if name.lower() in model.name.lower():
                return model
        return None

    def show_models_table(self, current_model: str = None):
        """Display models in a rich table"""
        models = self.get_models()

        if not models:
            self.console.print("[yellow]No models available[/yellow]")
            return

        table = Table(title="Available Models")
        table.add_column("Model Name", style="cyan", no_wrap=True)
        table.add_column("Size", style="green")
        table.add_column("Modified", style="dim")
        table.add_column("Status", style="bold")

        for model in models:
            status = "← current" if current_model and model.name == current_model else ""
            table.add_row(model.name, model.size, model.modified_at, status)

        self.console.print(table)

    def pull_model(self, model_name: str) -> bool:
        """Pull a model from registry"""
        try:
            self.console.print(f"[blue]Pulling model: {model_name}...[/blue]")

            # This would require streaming the pull request
            # For now, just show the command
            self.console.print(f"[yellow]Run this command to pull the model:[/yellow]")
            self.console.print(f"[green]ollama pull {model_name}[/green]")

            # After pulling, refresh cache
            time.sleep(1)  # Brief pause
            self.refresh_models(force=True)
            return True

        except Exception as e:
            self.console.print(f"[red]Error pulling model: {e}[/red]")
            return False

    def remove_model(self, model_name: str) -> bool:
        """Remove a model"""
        try:
            r = requests.delete(f"{self.base_url}/api/delete", json={"name": model_name})
            r.raise_for_status()
            self.refresh_models(force=True)
            self.console.print(f"[green]Removed model: {model_name}[/green]")
            return True
        except Exception as e:
            self.console.print(f"[red]Error removing model: {e}[/red]")
            return False