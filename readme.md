

## Don't Touch the Don't Touch Directoy 🙄😂 ❗❗

# WhatsAutoX

**WhatsAuto** is a command-line tool that automates the process of sending WhatsApp messages using WhatsApp Web. The tool uses image-based recognition to ensure the correct status of WhatsApp Web, such as checking if the user is logged in, and handles invalid numbers automatically.

## Features
- **Automated Messaging:** Send messages to multiple recipients via WhatsApp Web.

- **Flexible Input:** Use a text file for phone numbers and messages, or input them directly via the command line.
- **Cross-Platform:** Works on both Windows and Linux.

## Installation

- . **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/whatsauto.git
   cd whatsauto

- . **Install Required Packages:** 
    - Ensure you have Python 3.6+
    - Install the required dependencies using pip
    ```bash
    pip install -r requirements.txt

- . **Make the Script Executable (Linux):**
    To run the tool from anywhere in Linux, you need to make the 
    script executable and add it to your PATH:
    
    ```bash
    chmod +x send_whatsapp.py
    sudo ln -s $(PWD)/send_whatsapp.py /usr/local/bin/send_whatsapp

- . **Run the Tool:**
    You can now execute the tool from any directory

    ```bash
    send_whatsapp --message-file message.txt --phone-numbers-file numbers.txt

## Usage

To use WhatsAuto, you can provide either a message file and a phone numbers file, or input the message directly from the command line.

-  **Basic Command**:
    ```bash
    python send_whatsapp.py --message "Hello, this is a test message!" --phone-numbers-file numbers.txt

- **Using a Message File**:
    ```bash
    python send_whatsapp.py --message-file message.txt --phone-numbers-file numbers.txt

- **Manual Phone Number Input:** if you do not provide phone numbers file, the tool will prompt you to enter number manually.

## Options:

- '--message-file': Path to the text file containing the message.
- '--phone-numbers-file': Path to the text file containing phone numbers.
- '--message': Directly pass the message as a command-line argument.

