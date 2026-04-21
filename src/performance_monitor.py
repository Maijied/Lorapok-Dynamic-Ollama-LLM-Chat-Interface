import time
import psutil
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live

@dataclass
class PerformanceMetrics:
    response_time: float
    tokens_generated: int
    tokens_per_second: float
    model_name: str
    timestamp: float

class DynamicPerformanceMonitor:
    def __init__(self, base_url: str, console: Console):
        self.base_url = base_url
        self.console = console
        self.metrics_history: List[PerformanceMetrics] = []
        self.max_history = 50

    def measure_generation(self, prompt: str, model: str) -> Optional[PerformanceMetrics]:
        """Measure performance of a generation request"""
        start_time = time.time()

        try:
            # Make the request and measure
            r = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=300
            )
            r.raise_for_status()

            end_time = time.time()
            response_time = end_time - start_time

            data = r.json()
            response_text = data.get("response", "")
            # Estimate tokens (rough approximation)
            tokens_generated = len(response_text.split()) * 1.3  # Rough token estimation

            tokens_per_second = tokens_generated / response_time if response_time > 0 else 0

            metrics = PerformanceMetrics(
                response_time=response_time,
                tokens_generated=int(tokens_generated),
                tokens_per_second=tokens_per_second,
                model_name=model,
                timestamp=end_time
            )

            self.metrics_history.append(metrics)
            if len(self.metrics_history) > self.max_history:
                self.metrics_history = self.metrics_history[-self.max_history:]

            return metrics

        except Exception as e:
            self.console.print(f"[red]Performance measurement failed: {e}[/red]")
            return None

    def get_system_stats(self) -> Dict:
        """Get current system statistics"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            return {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "memory_used_gb": round(memory.used / (1024**3), 2),
                "memory_total_gb": round(memory.total / (1024**3), 2),
                "disk_percent": disk.percent,
                "disk_used_gb": round(disk.used / (1024**3), 2),
                "disk_total_gb": round(disk.total / (1024**3), 2)
            }
        except Exception as e:
            return {"error": str(e)}

    def show_performance_stats(self):
        """Display performance statistics"""
        if not self.metrics_history:
            self.console.print("[yellow]No performance data available[/yellow]")
            return

        # Calculate averages
        total_requests = len(self.metrics_history)
        avg_response_time = sum(m.response_time for m in self.metrics_history) / total_requests
        avg_tokens = sum(m.tokens_generated for m in self.metrics_history) / total_requests
        avg_tokens_per_sec = sum(m.tokens_per_second for m in self.metrics_history) / total_requests

        # Create stats table
        stats_table = Table(title="Performance Statistics")
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="green")

        stats_table.add_row("Total Requests", str(total_requests))
        stats_table.add_row("Avg Response Time", f"{avg_response_time:.2f}s")
        stats_table.add_row("Avg Tokens Generated", f"{avg_tokens:.0f}")
        stats_table.add_row("Avg Tokens/Second", f"{avg_tokens_per_sec:.1f}")

        self.console.print(stats_table)

        # Show recent requests
        recent_table = Table(title="Recent Requests")
        recent_table.add_column("Model", style="cyan", width=20)
        recent_table.add_column("Response Time", style="green")
        recent_table.add_column("Tokens", style="yellow")
        recent_table.add_column("Tokens/Sec", style="magenta")

        for metric in self.metrics_history[-5:]:  # Last 5
            recent_table.add_row(
                metric.model_name[:19] + "..." if len(metric.model_name) > 19 else metric.model_name,
                f"{metric.response_time:.2f}s",
                str(metric.tokens_generated),
                f"{metric.tokens_per_second:.1f}"
            )

        self.console.print(recent_table)

    def show_system_stats(self):
        """Display system statistics"""
        stats = self.get_system_stats()

        if "error" in stats:
            self.console.print(f"[red]Could not get system stats: {stats['error']}[/red]")
            return

        system_table = Table(title="System Statistics")
        system_table.add_column("Component", style="cyan")
        system_table.add_column("Usage", style="green")
        system_table.add_column("Details", style="yellow")

        system_table.add_row(
            "CPU",
            f"{stats['cpu_percent']:.1f}%",
            "Current usage"
        )
        system_table.add_row(
            "Memory",
            f"{stats['memory_percent']:.1f}%",
            f"{stats['memory_used_gb']}GB / {stats['memory_total_gb']}GB"
        )
        system_table.add_row(
            "Disk",
            f"{stats['disk_percent']:.1f}%",
            f"{stats['disk_used_gb']}GB / {stats['disk_total_gb']}GB"
        )

        self.console.print(system_table)

    def benchmark_model(self, model: str, test_prompts: List[str] = None) -> Dict:
        """Benchmark a model's performance"""
        if test_prompts is None:
            test_prompts = [
                "Hello, how are you?",
                "Write a short poem about AI.",
                "Explain quantum computing in simple terms.",
                "What is the capital of France?"
            ]

        self.console.print(f"[blue]Benchmarking model: {model}[/blue]")

        results = []
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task("Running benchmarks...", total=len(test_prompts))

            for prompt in test_prompts:
                metrics = self.measure_generation(prompt, model)
                if metrics:
                    results.append(metrics)
                progress.advance(task)

        if not results:
            return {"error": "No successful benchmarks"}

        # Calculate averages
        avg_time = sum(r.response_time for r in results) / len(results)
        avg_tokens = sum(r.tokens_generated for r in results) / len(results)
        avg_tps = sum(r.tokens_per_second for r in results) / len(results)

        benchmark_result = {
            "model": model,
            "test_count": len(results),
            "avg_response_time": round(avg_time, 2),
            "avg_tokens": round(avg_tokens, 0),
            "avg_tokens_per_second": round(avg_tps, 2),
            "total_tokens": sum(r.tokens_generated for r in results)
        }

        # Display results
        bench_table = Table(title=f"Benchmark Results: {model}")
        bench_table.add_column("Metric", style="cyan")
        bench_table.add_column("Value", style="green")

        bench_table.add_row("Test Prompts", str(benchmark_result["test_count"]))
        bench_table.add_row("Avg Response Time", f"{benchmark_result['avg_response_time']}s")
        bench_table.add_row("Avg Tokens", str(benchmark_result["avg_tokens"]))
        bench_table.add_row("Avg Tokens/Second", str(benchmark_result["avg_tokens_per_second"]))
        bench_table.add_row("Total Tokens", str(benchmark_result["total_tokens"]))

        self.console.print(bench_table)

        return benchmark_result