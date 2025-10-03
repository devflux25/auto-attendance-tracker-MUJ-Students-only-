# auto-attendance-tracker-MUJ-Students-only-
A Python bot using Selenium and PyAutoGUI that automatically collects attendance data from SLCM and sends it to WhatsApp. Note: This script works only for MUJ students with valid SLCM credentials.

# Attendance Collector Bot (MUJ Students Only)

This bot automatically collects your attendance from **SLCM** and sends it to **WhatsApp Web**.
It is built using **Selenium** and **PyAutoGUI**.

⚠️ **Note:** This bot only works if you are an MUJ student with valid SLCM credentials.

---

## Requirements

Before running the bot, make sure you have:

* Google Chrome installed
* Logged into **WhatsApp Web** on Google Chrome
* Python 3.8+ installed

Install the required Python packages:

```bash
pip install selenium
pip install pyautogui
pip install pywin32
```

---

## How It Works

1. The bot logs into SLCM with your credentials.
2. It collects your attendance data.
3. It sends the data to your WhatsApp Web contact.

---

## Usage

1. Clone this repository:

   ```bash
   git clone 
   cd your-repo
   ```
2. Add your SLCM credentials and WhatsApp contact details inside `bot.py`.
3. Run the bot:

   ```bash
   python bot.py
   ```

---

## Disclaimer

* This script is for **educational purposes only**.
* It will only work for MUJ students who have access to SLCM.
* Use responsibly.
