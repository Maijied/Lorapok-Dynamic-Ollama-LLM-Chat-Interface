#!/usr/bin/env python3
"""
Lorapok Dynamic Ollama LLM Chat Interface - Test Suite

This script runs comprehensive tests to ensure all components work correctly.
"""

import sys
import os
import json
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all module imports"""
    print("🧪 Testing imports...")
    try:
        from config import DynamicConfig
        from model_manager import DynamicModelManager, ModelInfo
        from conversation_manager import DynamicConversationManager, Message
        from performance_monitor import DynamicPerformanceMonitor, PerformanceMetrics
        from ollama_client import OllamaClient
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_config():
    """Test configuration system"""
    print("🧪 Testing configuration system...")
    try:
        from config import DynamicConfig
        config = DynamicConfig()

        # Test loading
        cfg = config.get_config()
        assert cfg.server_ip == "192.168.0.219"
        assert cfg.default_model == "qwen2.5-coder:7b-instruct"

        # Test updating
        old_timeout = cfg.timeout
        config.update_config("timeout", 300)
        cfg = config.get_config()
        assert cfg.timeout == 300

        # Reset
        config.update_config("timeout", old_timeout)

        print("✅ Configuration system working")
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_conversation_manager():
    """Test conversation management"""
    print("🧪 Testing conversation manager...")
    try:
        from conversation_manager import DynamicConversationManager, Message
        from rich.console import Console

        console = Console()
        cm = DynamicConversationManager(console)

        # Test adding messages
        cm.add_message("user", "Hello", "test-model", 10, 1.5)
        cm.add_message("assistant", "Hi there!", "test-model", 15, 2.0)

        # Test stats
        stats = cm.get_conversation_stats()
        assert stats["total_messages"] == 2
        assert stats["user_messages"] == 1
        assert stats["assistant_messages"] == 1

        # Test search
        results = cm.search_messages("Hello")
        assert len(results) == 1

        print("✅ Conversation manager working")
        return True
    except Exception as e:
        print(f"❌ Conversation manager test failed: {e}")
        return False

def test_model_manager():
    """Test model management (without actual Ollama server)"""
    print("🧪 Testing model manager...")
    try:
        from model_manager import DynamicModelManager, ModelInfo
        from rich.console import Console

        console = Console()
        # Test with invalid URL to avoid actual connection
        mm = DynamicModelManager("http://invalid-url:11434", console)

        # Test model info creation
        model = ModelInfo("test-model", "1.2GB", "2024-01-01", "digest123")
        assert model.name == "test-model"

        # Test model finding
        found = mm.find_model("nonexistent")
        assert found is None

        print("✅ Model manager structure working")
        return True
    except Exception as e:
        print(f"❌ Model manager test failed: {e}")
        return False

def test_performance_monitor():
    """Test performance monitoring"""
    print("🧪 Testing performance monitor...")
    try:
        from performance_monitor import DynamicPerformanceMonitor, PerformanceMetrics
        from rich.console import Console

        console = Console()
        pm = DynamicPerformanceMonitor("http://invalid-url:11434", console)

        # Test metrics creation
        metrics = PerformanceMetrics(2.5, 150, 60.0, "test-model", 1234567890)
        assert metrics.response_time == 2.5
        assert metrics.tokens_generated == 150

        # Test system stats (may fail on some systems)
        try:
            stats = pm.get_system_stats()
            assert "cpu_percent" in stats
            print("✅ Performance monitor and system stats working")
        except:
            print("⚠️ Performance monitor working (system stats not available)")

        return True
    except Exception as e:
        print(f"❌ Performance monitor test failed: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("🧪 Testing file structure...")
    required_files = [
        "README.md",
        "requirements.txt",
        "package.json",
        "config.json",
        ".gitignore",
        "src/ollama_client.py",
        "src/config.py",
        "src/model_manager.py",
        "src/conversation_manager.py",
        "src/performance_monitor.py",
        "docs/setup.md",
        "docs/usage.md",
        "docs/api.md",
        "setup/install_dependencies.ps1",
        "scripts/run_server.ps1",
        "scripts/connect_client.ps1",
        "chat.sh"
    ]

    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Lorapok Dynamic Ollama LLM Chat Interface Test Suite")
    print("=" * 70)

    tests = [
        test_file_structure,
        test_imports,
        test_config,
        test_conversation_manager,
        test_model_manager,
        test_performance_monitor,
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")

    print("=" * 70)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Ready for deployment.")
        return True
    else:
        print("⚠️ Some tests failed. Please review before deployment.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)