# HexGemini Installer

This project automates the installation and configuration of the HexStrike offensive security framework and integrates it with the Gemini CLI on a Linux system.

## Features

- **Automated Installation:** A single script to install HexStrike and all of its Python dependencies.
- **Automated Patching:** Automatically applies necessary patches to the `hexstrike_server.py` to ensure it runs correctly.
- **Automated Gemini CLI Configuration:** Automatically configures the Gemini CLI to recognize and use the `@hexstrike-ai` agent.

## Getting Started (Linux)

Follow these beginner-friendly steps to set up HexGemini on your Linux machine.

### Prerequisites

*   **Linux Operating System:** This guide assumes you are running a Debian-based Linux distribution (like Ubuntu, Kali Linux, or Linux Mint).
*   **Basic Terminal Knowledge:** You should know how to open a terminal and execute commands.
*   **Git:** Used to clone the repository.

### Step 1: Open a Terminal

Open your terminal application. You can usually find it in your applications menu or by pressing `Ctrl+Alt+T`.

### Step 2: Install Git (if you don't have it)

If you don't have Git installed, use the following command:

```bash
sudo apt update
sudo apt install git -y
```

### Step 3: Clone the Repository

Navigate to the directory where you want to store the project (e.g., your home directory). Then, clone this repository:

```bash
cd ~ # Go to your home directory (optional)
git clone https://github.com/SpitFiyah/HexGemini.git
cd HexGemini
```

### Step 4: Run the Installation Script

Now, execute the installation script. This script will set up everything required for HexStrike and its integration with the Gemini CLI.

```bash
python3 install.py
```
The script will perform the following actions:
-   Verify that your operating system is Linux.
-   Create a isolated Python virtual environment named `hexstrike-env` inside the `hexstrike` directory.
-   Install all the necessary Python dependencies for HexStrike.
-   Apply crucial compatibility patches to the `hexstrike_server.py` file to ensure smooth operation.
-   Configure your Gemini CLI to automatically recognize and work with the `@hexstrike-ai` agent.

## Usage

### 1. Start the HexStrike Server

Before you can use the `@hexstrike-ai` agent in the Gemini CLI, you **must** start the HexStrike server. Open a **new terminal window** and run the following command:

```bash
./hexstrike/hexstrike-env/bin/python ./hexstrike/hexstrike_server.py
```
**Important:** Keep this terminal window open and running in the background for as long as you want to use the HexStrike tools via the Gemini CLI.

### 2. Use the `@hexstrike-ai` Agent in Gemini CLI

Once the server is running, you can interact with HexStrike directly from your Gemini CLI sessions. Just invoke the `@hexstrike-ai` agent followed by the command you wish to execute.

**Example:** Perform an Nmap scan with OS detection and version detection on `scanme.nmap.org`:

```
@hexstrike-ai nmap -A -T4 scanme.nmap.org
```

## Contributing / Setting up Your Own Fork

If you wish to contribute to this project or set up your own customizable fork, you can:

1.  **Fork this repository** on GitHub.
2.  **Clone your forked repository** to your local machine.
3.  Make your desired changes.
4.  Commit and push your changes to your fork.
5.  Consider opening a Pull Request to share your enhancements!