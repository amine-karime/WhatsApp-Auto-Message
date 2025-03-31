
import pywhatkit as pwk
import time

# List of phone numbers (with country codes)
phone_numbers = [
    "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX",
    "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX",
    "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX",
    "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX",
    "+212XXXXXXXXX", "+212XXXXXXXXX", "+212XXXXXXXXX"
]

# Message to send
message = "Eid Mubarak! ❤️"

# Send messages with a 5-second delay
for number in phone_numbers:
    try:
        pwk.sendwhatmsg_instantly(number, message)
        print(f"Message sent to {number}")
        time.sleep(5)  # Wait 5 seconds before next message
    except Exception as e:
        print(f"Failed to send to {number}: {e}")
