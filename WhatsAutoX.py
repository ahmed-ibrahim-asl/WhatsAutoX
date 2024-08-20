import os
from platform import system
import argparse
import pyautogui
import webbrowser as web

from urllib.parse import quote
from time import sleep


skipped_numbers = []

def locate_and_click_send_button():
    """
    Locates the 'Send' button on the screen and clicks it.
    """
    try:
        button_location = pyautogui.locateCenterOnScreen("Don't Touch/send_button_image.jpg", confidence=0.8)

        if button_location is not None:
            pyautogui.click(button_location)
            return True
            
        else:
            raise pyautogui.ImageNotFoundException("Could not locate the send button image.")
            return False
    
    except Exception as e:
        print(f"An error occurred: {e}")
        skipped_numbers.append(current_number)
        return False


def check_for_invalid_number():
    """
    Checks for the "Invalid Number" pop-up and closes it if found.
    Returns True if the number is invalid, otherwise False.
    """
    try:
        invalid_popup = pyautogui.locateCenterOnScreen("Don't Touch/invalid_number_image.jpg", confidence=0.8)
        
        if invalid_popup is not None:
            pyautogui.click(invalid_popup)

            print("Invalid phone number detected.")

            return True

        return False

    except Exception as e:

        print(f"An error occurred while checking for invalid number: {e}")
        return False


def is_whatsapp_Notlogged_in():
    try:
        invalid_popup = pyautogui.locateCenterOnScreen("Don't Touch/not_loggedIn.jpg", confidence=0.8)
        
        if invalid_popup is not None:
            pyautogui.click(invalid_popup)

            return True

        return False

    except Exception as e:

        print(f"An error occurred while checking for invalid number: {e}")
        return False
    return True 



def send_whatsapp_message(phone_no, message, wait_time=20, close_time=3):
    """
        -wait_time:  Time(seconds), to wait for the whatsapp web page to fully load before start sending the message.
        -close_time: Time(seconds), to sending time for message to ensure it's has been sent correctly before close. 
    """
    global current_number
    current_number = phone_no
    
    if not phone_no:
        print("Phone number is empty, skipping...")
        skipped_numbers.append(phone_no)
        return
    
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    sleep(wait_time)


    if is_whatsapp_Notlogged_in():
        print("WhatsApp Web is not logged in")
        exit(1)


    if check_for_invalid_number():
        print(f"Skipping invalid number: {phone_no}")
        skipped_numbers.append(phone_no)
        pyautogui.hotkey('ctrl', 'w')
        return


    if(locate_and_click_send_button()):
        print(f"Message has been sent to {phone_no}")

    sleep(close_time)
    pyautogui.hotkey('ctrl', 'w')

def read_message_from_file(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def read_phone_numbers_from_file(filepath):

    phone_numbers = []
    with open(filepath, 'r', encoding='utf-8') as file:

        for line in file:

            stripped_line = line.strip()
            if stripped_line:
                phone_numbers.append(stripped_line)


        return phone_numbers

def export_skipped_numbers(filepath):
    """
    Exports the skipped phone numbers to a file.
    """
    if skipped_numbers:

        with open(filepath, 'w', encoding='utf-8') as file:
        
            for number in skipped_numbers:
        
                file.write(f"{number}\n")



#Message get printed when passing '-h' parameter
parser = argparse.ArgumentParser(description="Send WhatsApp messages automatically via command line.")


# Obviously this to define new parameter, (syntax: argumentName, default_value, description for this parameter)
# Nargs '?' means argument can take zero or one value it's like defining it's optional parameter 
parser.add_argument('--message-file', nargs='?', default=None, help="Path to the text file containing the message.")

parser.add_argument('--phone-numbers-file', nargs='?', default=None, help="Path to the text file containing phone numbers.")

parser.add_argument('--message', nargs='?', default=None, help="Directly pass the message as a command-line argument.")



# parse_args: method that process input acordingly to defined rules 
args = parser.parse_args()


# Read the message
if args.message_file:

    if os.path.exists(args.message_file):
        message_body = read_message_from_file(args.message_file)
        
    else:
        print(f"Message file '{args.message_file}' does not exist.")
        exit(1)
    
elif args.message:
    message_body = args.message
    
else:
    print("No message provided. Please provide a message file or use the --message option.")
    exit(1)
    
# Read or input phone numbers
if args.phone_numbers_file:

    if os.path.exists(args.phone_numbers_file):
        recipient_numbers = read_phone_numbers_from_file(args.phone_numbers_file)

    else:
        print(f"Phone numbers file '{args.phone_numbers_file}' does not exist.")
        exit(1)

else:
    recipient_numbers = []
        
    print("No phone numbers file provided. Enter numbers manually.")
    while True:
            
        number = input("Enter phone number (or press Enter to finish): ")
        if number:
            recipient_numbers.append(number)
        else:
            
            if system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')

            break
    
    # Loop through the list of numbers and send the message to each one
    
    counter = 0
    for number in recipient_numbers:
        
        print(f"Sending a message to {number}")
        send_whatsapp_message(number, message_body)

        sleep(20)  # Adjust based on your system speed and network latency
    
    # Export skipped numbers to a file
    export_skipped_numbers('skipped_numbers.txt')
    print("Process completed. Skipped numbers have been saved to 'skipped_numbers.txt'.")

