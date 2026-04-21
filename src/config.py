import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

@dataclass
class Config:
    server_ip: str = "192.168.0.219"
    default_model: str = "qwen2.5-coder:7b-instruct"
    max_history: int = 100
    auto_save: bool = True
    theme: str = "default"
    show_timestamps: bool = True
    stream_responses: bool = True
    timeout: int = 120
    max_retries: int = 3

class DynamicConfig:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = Config()
        self.load_config()

    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    # Update config with loaded data
                    for key, value in data.items():
                        if hasattr(self.config, key):
                            setattr(self.config, key, value)
            except Exception as e:
                print(f"Warning: Could not load config: {e}")

    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(asdict(self.config), f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config: {e}")

    def update_config(self, key: str, value):
        """Update a configuration value"""
        if hasattr(self.config, key):
            setattr(self.config, key, value)
            self.save_config()
            return True
        return False

    def get_config(self) -> Config:
        """Get current configuration"""
        return self.config

    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = Config()
        self.save_config()