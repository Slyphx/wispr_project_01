import pyautogui
import time
import random

FILE_PATH = r"D:\\large dev\\audio projects\\code.txt"

START_DELAY = 5      # seconds to switch to editor
BASE_DELAY = 0.03    # delay between normal characters
PUNCT_DELAY = 0.08   # delay for punctuation characters

print(f"Starting in {START_DELAY} seconds. Focus your editor window...")
time.sleep(START_DELAY)

# Read file line by line
with open(FILE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Characters that need slightly longer delay
punctuation = set("(){}[]=;,.\"'")

for line in lines:
    for char in line:
        pyautogui.typewrite(char)
        if char in punctuation:
            time.sleep(PUNCT_DELAY)
        else:
            time.sleep(BASE_DELAY)
    pyautogui.press("enter")
    time.sleep(random.uniform(0.05, 0.15))  # small random delay between lines

print("✅ Typing finished.")

