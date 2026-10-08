import time
import RPi.GPIO as GPIO
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
#print(BOT_TOKEN)
CHAT_ID = os.getenv("CHAT_ID")
#print(CHAT_ID)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

api_address = (f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage")

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH:
            print("Someone pressed the alert button!")
            requests.post(api_address,json = {"chat_id":CHAT_ID,"text":"Someone pressed the alert button!"})
            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()
