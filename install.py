
#!/usr/bin/env python3
import os
import subprocess
import sys
import pathlib
import json

# --- Constants ---
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
HEXSTRIKE_DIR = PROJECT_ROOT / "hexstrike"
VENV_DIR = HEXSTRIKE_DIR / "hexstrike-env"
PIP_EXEC = VENV_DIR / "bin" / "pip"
PYTHON_EXEC = VENV_DIR / "bin" / "python"
HEXSTRIKE_SERVER_PY = HEXSTRIKE_DIR / "hexstrike_server.py"
HEXSTRIKE_MCP_PY = HEXSTRIKE_DIR / "hexstrike_mcp.py"
GEMINI_CONFIG_DIR = pathlib.Path.home() / ".config" / "google" / "gemini"
GEMINI_SETTINGS_JSON = GEMINI_CONFIG_DIR / "settings.json"
HEXSTRIKE_MCP_JSON = HEXSTRIKE_DIR / "hexstrike-ai-mcp.json"

# --- Helper Functions ---

def print_step(message):
    """Prints a formatted step message."""
    print(f"\n{'='*60}")
    print(f"  {message}")
    print(f"{ '='*60}\n")

def run_command(command, cwd=None):
    """Runs a command and handles errors."""
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

# --- Installation Steps ---

def check_linux():
    """Checks if the script is running on Linux."""
    print_step("Checking Operating System...")
    if sys.platform != "linux":
        print("This installation script is designed for Linux only.")
        sys.exit(1)
    print("Operating system check passed (Linux).")

def install_gemini_cli():
    """Placeholder for Gemini CLI installation."""
    print_step("Installing Gemini CLI...")
    print("NOTE: A standalone Gemini CLI for Linux is not yet officially available.")
    print("This script assumes you have a method for installing it, or that you")
    print("will install it manually. For now, we will proceed.")
    # Here you would add the actual installation command when it's available
    # For example:
    # run_command("pip install google-generativeai-cli")

def setup_hexstrike_venv():
    """Creates a virtual environment and installs dependencies."""
    print_step("Setting up HexStrike virtual environment...")
    run_command(f"python3 -m venv {VENV_DIR}")
    print("Virtual environment created.")
    
    print("Installing HexStrike dependencies...")
    dependencies = [
        "flask", "requests", "psutil", "fastmcp", "beautifulsoup4", 
        "selenium", "webdriver-manager", "aiohttp", "mitmproxy", 
        "pwntools", "angr", "bcrypt==4.0.1"
    ]
    run_command(f"{PIP_EXEC} install {' '.join(dependencies)}")
    print("Dependencies installed.")

def patch_hexstrike_server():
    """Patches the hexstrike_server.py file."""
    print_step("Patching hexstrike_server.py for compatibility...")
    with open(HEXSTRIKE_SERVER_PY, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add imports
    content = content.replace('import logging', 'import logging\nimport os\nimport tempfile\nimport sys')
    # Fix logging
    content = content.replace("logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')", "logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')")
    # Fix init methods
    content = content.replace('def __init__(self, base_dir: str = "/tmp/hexstrike_envs"):', 'def __init__(self, base_dir=None):\n        if base_dir is None:\n            base_dir = os.path.join(tempfile.gettempdir(), "hexstrike_envs")')
    content = content.replace('def __init__(self, base_dir: str = "/tmp/hexstrike_files"):', 'def __init__(self, base_dir=None):\n        if base_dir is None:\n            base_dir = os.path.join(tempfile.gettempdir(), "hexstrike_files")')
    # Fix other /tmp paths
    content = content.replace('"/tmp/"', 'os.path.join(tempfile.gettempdir(), "')
    
    with open(HEXSTRIKE_SERVER_PY, 'w', encoding='utf-8') as f:
        f.write(content)
    print("hexstrike_server.py patched successfully.")

def configure_gemini_integration():
    """Configures the Gemini CLI to integrate with HexStrike."""
    print_step("Configuring Gemini CLI integration...")

    # Create hexstrike-ai-mcp.json
    mcp_config = {
        "mcpServers": {
            "hexstrike-ai": {
                "command": str(PYTHON_EXEC),
                "args": [
                    str(HEXSTRIKE_MCP_PY),
                    "--server",
                    "http://127.0.0.1:8888"
                ],
                "description": "HexStrike AI v6.0 - Advanced Cybersecurity Automation Platform.",
                "timeout": 300,
                "alwaysAllow": []
            }
        }
    }
    with open(HEXSTRIKE_MCP_JSON, 'w') as f:
        json.dump(mcp_config, f, indent=2)
    print("Created hexstrike-ai-mcp.json.")

    # Update Gemini settings.json
    GEMINI_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    settings = {}
    if GEMINI_SETTINGS_JSON.exists():
        with open(GEMINI_SETTINGS_JSON, 'r') as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                print("Warning: Existing Gemini settings.json is corrupted. A new one will be created.")

    if "mcp" not in settings:
        settings["mcp"] = {"configs": []}
    
    mcp_config_path = str(HEXSTRIKE_MCP_JSON)
    if mcp_config_path not in settings["mcp"]["configs"]:
        settings["mcp"]["configs"].append(mcp_config_path)

    with open(GEMINI_SETTINGS_JSON, 'w') as f:
        json.dump(settings, f, indent=2)
    print("Updated Gemini CLI settings.json.")


def main():
    """Main function to orchestrate the installation."""
    check_linux()
    install_gemini_cli()
    setup_hexstrike_venv()
    patch_hexstrike_server()
    configure_gemini_integration()
    print("\n\nInstallation complete!")
    print("Please see README.md for instructions on how to run the server and use the tool.")

if __name__ == "__main__":
    main()
