import os
import re

from platform import system 


def format_number_with_country_code(number: str) -> str:
    """
    Identify the country based on the given phone number prefix and format the number with the correct country code.
    
    :param number: The phone number without the country code
    :return: A string indicating the formatted phone number with the country code
    """
    
    # Define known prefixes and corresponding country codes
    prefixes = {
        'Egypt': {'code': '+2',
        'prefixes': ['010', '011', '012', '015'] },
        
        'UK'   : {'code': '+44',
        'prefixes': ['07']},
        
        'USA/Canada': {'code': '+1',
        'prefixes': ['201', '202', '212', '213', '310', '415', '510']},
        
        'Germany': {'code': '+49',
        'prefixes': ['0151', '0160', '0170']},
        
        'India': {'code': '+91',
        'prefixes': ['098', '099']},
        
        'Australia': {'code': '+61',
        'prefixes': ['04']},
        
        'France': {'code': '+33',
        'prefixes': ['06', '07']},
        
        'China': {'code': '+86',
        'prefixes': ['13', '14', '15', '16', '17', '18', '19']},
        
        'Brazil': {'code': '+55',
        'prefixes': ['6', '7', '8', '9']},
        
        'Saudi Arabia': {'code': '+966',
        'prefixes': ['050', '053', '054', '055', '056', '057', '058']},
        
        'United Arab Emirates': {'code': '+971',
        'prefixes': ['050', '055', '056']},
        
        'Qatar': {'code': '+974',
        'prefixes': ['33', '44', '55', '66', '77']},
        
        'South Africa': {'code': '+27',
        'prefixes': ['071', '072', '073', '074', '081', '082', '083', '084']},
        
        'Japan': {'code': '+81',
        'prefixes': ['070', '080', '090']},
        
        'South Korea': {'code': '+82',
        'prefixes': ['010', '011', '016', '017', '018', '019']},
        
        'Russia': {'code': '+7',
        'prefixes': ['901', '902', '903', '904', '905', '906', '909']}
        
        # More countries can be added here
    }

    
    # Matches any non-digit character and replaces it with an empty string in the number
    normalized_number = re.sub(r'\D', '', number)
    

    for country, data in prefixes.items():

        for prefix in data['prefixes']:
            if number.startswith(prefix):
                return f"{country},{data['code']}{number}".split(',')

    return "Country could not be identified."



if __name__ == "__main__":
    
    if system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
    while True:
        
        print("\nPlease choose an option:")
        print("1. Update the database")
        print("2. Use the program")
        print("3. Exit")
        
        user_input_choice = input("Enter your choice (1/2/3): ").strip()
        
        
        if user_input_choice == '1':
            #! "I am still working on this part"
            pass 
        
        elif user_input_choice == '2':
            user_input_phoneNumber = input("\nEnter the number without country code\nLet Me try to get it: ").strip()
            
            if user_input_phoneNumber.isdigit():
                result = format_number_with_country_code(user_input_phoneNumber)
                
                if isinstance(result, list):
                    print(f"Country: {result[0]}, Formatted Number: {result[1]}")
                    
                else:
                    print(result)
            
            else:
                print("Please enter a valid number consisting only of digits.")
                    
        
        elif user_input_choice == '3':
            print("Exiting the program. Goodbye!")
            break
    
    else:
        print("Invalid choice, please try again.")
        
        