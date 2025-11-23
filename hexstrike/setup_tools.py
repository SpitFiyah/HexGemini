import shutil
import subprocess
import sys
import os

TOOLS = {
    "nmap": {"cmd": "nmap", "winget": "Insecure.Nmap"},
    "masscan": {"cmd": "masscan", "winget": "masscan"}, # check winget id
    "nuclei": {"cmd": "nuclei", "winget": "ProjectDiscovery.Nuclei"},
    "gobuster": {"cmd": "gobuster", "winget": "OJ.Gobuster"},
    "sqlmap": {"cmd": "sqlmap", "winget": "sqlmap"},
    "ffuf": {"cmd": "ffuf", "winget": "ffuf"},
    "httpx": {"cmd": "httpx", "winget": "ProjectDiscovery.httpx"},
}

def check_tool(tool_name, tool_info):
    if shutil.which(tool_info["cmd"]):
        print(f"[+] {tool_name} is installed.")
        return True
    return False

def install_tool(tool_name, tool_info):
    print(f"[*] Attempting to install {tool_name}...")
    
    # Try Winget
    if shutil.which("winget"):
        print(f"    Running winget install {tool_info['winget']}...")
        try:
            subprocess.run(["winget", "install", "-e", "--id", tool_info["winget"], "--accept-source-agreements", "--accept-package-agreements"], check=True)
            print(f"[+] {tool_name} installed via Winget.")
            return True
        except subprocess.CalledProcessError:
            print(f"[-] Winget installation failed for {tool_name}.")
    
    # Try Choco as fallback
    if shutil.which("choco"):
        print(f"    Running choco install {tool_name}...")
        try:
            subprocess.run(["choco", "install", tool_name, "-y"], check=True)
            print(f"[+] {tool_name} installed via Chocolatey.")
            return True
        except subprocess.CalledProcessError:
            print(f"[-] Chocolatey installation failed for {tool_name}.")

    print(f"[!] Could not install {tool_name}. Please install manually.")
    return False

def main():
    print("Checking for required security tools...")
    missing = []
    for name, info in TOOLS.items():
        if not check_tool(name, info):
            missing.append(name)
    
    if not missing:
        print("\nAll tools are installed!")
        return

    print(f"\nMissing tools: {', '.join(missing)}")
    print("Attempting auto-installation...")
    
    for name in missing:
        install_tool(name, TOOLS[name])

    print("\nTool setup complete. Please restart your terminal if you installed new tools.")

if __name__ == "__main__":
    main()
