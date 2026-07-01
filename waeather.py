import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

users = {}


def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        
        print(f"\n--- Weather for {city_name} ---")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False
def create_account(username, password):
    try:
        if not username or not password:
            print("Username and password cannot be empty!")
            return False
        if username in users:
            print(f"Account '{username}' already exists!")
            return False
        users[username] = password
        print(f"Account '{username}' created!")
        return True
    except Exception as e:
        print(f"Error creating account: {e}")
        return False


def login(username, password):
    try:
        if not username or not password:
            print("Username and password cannot be empty!")
            return False
        if username not in users:
            print(f"User '{username}' not found!")
            return False
        if users[username] == password:
            print(f"Login successful! Welcome, {username}!")
            return True
        print("Invalid password!")
        return False
    except Exception as e:
        print(f"Error logging in: {e}")
        return False


if __name__ == "__main__":
        while True:
            try:
                print("\n--- Menu ---")
                print("1. Login")
                print("2. Create Account")
                print("3. Exit")
                
                choice = input("Choose an option (1-3): ").strip()
                
                if choice == "1":
                    username = input("Enter username: ").strip()
                    password = input("Enter password: ").strip()
                    if login(username, password):
                        print(f"\n--- Welcome {username} ---")
                        city = input("Enter city name: ").strip()
                        get_weather(city)
                
                elif choice == "2":
                    username = input("Enter username: ").strip()
                    password = input("Enter password: ").strip()
                    create_account(username, password)
                
                elif choice == "3":
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid option! Please choose 1, 2, or 3.")
            
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
    
 