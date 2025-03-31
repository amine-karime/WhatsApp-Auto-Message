
# WhatsApp-Auto-Message

Are you tired of sending "Eid Mubarak!" to everyone you know? Worry no more! This is the solution.  
This Python script allows you to send "Eid Mubarak! ❤️" to multiple WhatsApp contacts instantly. With a simple and automated process, you can send messages to as many contacts as you need with a 5-second delay to avoid spam detection.

## ✨ Features
- Send personalized messages to multiple contacts at once.
- Uses **WhatsApp Web** for messaging.
- Automatically handles sending messages to a list of phone numbers.
- Configurable **5-second delay** between messages to avoid spam detection.
- Simple setup with no complex dependencies.

## ⚙️ Prerequisites
- **Python 3.x** installed on your system.
- **WhatsApp Web** must be open and logged in on your default browser.
- `pywhatkit` library installed.

## 📥 Installation
1. **Install Python 3.x**  
   If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

2. **Install `pywhatkit`**  
   Run the following command in your terminal:
   ```bash
   pip install pywhatkit
   ```

3. **Log in to WhatsApp Web**  
   Open WhatsApp Web and scan the QR code using your phone.

---

## 🚀 Usage

1. **Clone or Download the Script**  
   Clone the repository or download the script as a `.py` file:
   ```bash
   git clone https://github.com/your-username/WhatsApp-Auto-Message.git
   cd WhatsApp-Auto-Message
   ```

2. **Modify Phone Numbers**  
   Edit `send_eid_message.py` and replace the placeholder phone numbers with your contacts' numbers (include the country code, e.g., `+212XXXXXXXXX`).

3. **Customize the Message (Optional)**  
   You can change the `message` variable if you want to send a different greeting.

4. **Run the Script**  
   Run the script with the following command:
   ```bash
   python send_eid_message.py
   ```

   The script will send the message to each contact with a 5-second delay.

---

## 📋 Example Code

```python
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
```

---

## ⚠️ Important Notes
- Ensure WhatsApp Web is open and logged in before running the script.
- A stable internet connection is required.
- Adjust the delay (e.g., `time.sleep(5)`) if needed, but 5 seconds is recommended to avoid spam detection.

## 📄 License
This project is open-source. Feel free to modify and distribute it.
