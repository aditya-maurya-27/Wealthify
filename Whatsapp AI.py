from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import google.generativeai as genai
genai.configure(api_key='AIzaSyBU8RdqlMWvVAXTuBE4vFOeZ4FpsvlmWIo')
model = genai.GenerativeModel('gemini-1.5-flash')
global conversation_history
conversation_history=[]
EDGE_PATH = r"C:\Users\Dell\msedgedriver.exe"
profile_path = r"C:\Users\Dell\AppData\Local\Microsoft\Edge\User Data\Profile 1"
edge_options = Options()
edge_options.add_argument(f"user-data-dir={profile_path}")
service = Service(executable_path=EDGE_PATH)
driver = webdriver.Edge(service=service, options=edge_options)

def login_whatsapp():
    driver.get("https://web.whatsapp.com")
    print("Please scan the QR code")
    time.sleep(5)
    print("Logged in, proceeding to the next step...")

def send_message(contact_name, message):
    print(f"Sending message to {contact_name}")
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')
    search_box.send_keys(contact_name)
    time.sleep(2)
    print(f"Contact {contact_name} found, clicking on it...")

    contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
    contact.click()
    time.sleep(2)
    
    print("Typing message...")
    message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys(message + Keys.RETURN)
    print("Message sent!")

# Main workflow
login_whatsapp()
time.sleep(10)
# Example usage
send_message("Bhavesh Kanaujia", "Jai Shree Ram")
time.sleep(50)  # Wait for the message to be sent
print("Done")
