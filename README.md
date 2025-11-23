
# Gemini HexStrike Installer

This project automates the installation and configuration of the HexStrike offensive security framework and integrates it with the Gemini CLI on a Linux system.

## Features

- **Automated Installation:** A single script to install HexStrike and all of its Python dependencies.
- **Automated Patching:** Automatically applies necessary patches to the `hexstrike_server.py` to ensure it runs correctly.
- **Automated Gemini CLI Configuration:** Automatically configures the Gemini CLI to recognize and use the `@hexstrike-ai` agent.

## Installation

1.  **Clone this repository:**
    ```bash
    git clone <your-repo-url>
    cd gemini-hexstrike-installer
    ```

2.  **Run the installation script:**
    ```bash
    python3 install.py
    ```
    The script will:
    - Verify you are running on a Linux system.
    - Create a Python virtual environment inside the `hexstrike` directory.
    - Install all necessary dependencies.
    - Patch the `hexstrike_server.py` file.
    - Configure your Gemini CLI.

## Usage

1.  **Start the HexStrike Server:**
    Before you can use the `@hexstrike-ai` agent, you must start the HexStrike server in a separate terminal:
    ```bash
    ./hexstrike/hexstrike-env/bin/python ./hexstrike/hexstrike_server.py
    ```
    Keep this terminal window open while you are using the tool.

2.  **Use in Gemini CLI:**
    Once the server is running, you can use the `@hexstrike-ai` agent in your Gemini CLI sessions to perform reconnaissance, scanning, and other security tasks.

    Example:
    ```
    @hexstrike-ai nmap -A -T4 scanme.nmap.org
    ```

## Publishing to GitHub

To publish this project to your own GitHub repository, follow these steps:

1.  **Go to GitHub and create a new repository.** Do not initialize it with a README or any other files.

2.  **In your terminal, navigate to the `gemini-hexstrike-installer` directory.**

3.  **Initialize a new Git repository:**
    ```bash
    git init
    git add .
    git commit -m "Initial commit: Gemini HexStrike Installer"
    ```

4.  **Link the local repository to your GitHub repository:**
    ```bash
    git remote add origin <your-repo-url.git>
    git branch -M main
    ```

5.  **Push the project to GitHub:**
    ```bash
    git push -u origin main
    ```

Now your project is live on GitHub!
