import pyautogui
import time
import random

# Path to your code file
FILE_PATH = r"D:\\large dev\\audio projects\\code.txt"

# Time to switch to VM/editor window after running script
print("You have 5 seconds to focus cursor on VM editor...")
time.sleep(5)

# Read the code from file
with open(FILE_PATH, "r", encoding="utf-8") as f:
    code_lines = f.readlines()

# Type the code line by line
for line in code_lines:
    pyautogui.typewrite(line, interval=0.06)  # interval = delay per char
    # Add an extra Enter for line break if missing
    if not line.endswith("\n"):
        pyautogui.press("enter")
    
    # Optional: random small delay between lines
    time.sleep(random.uniform(0.05, 0.15))

print("✅ Done typing into VM!")
