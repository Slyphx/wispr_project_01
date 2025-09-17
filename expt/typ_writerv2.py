# paste_chunks.py
# Paste file contents to the active window using clipboard-based chunks.
# Usage: edit the FILENAME and run: python paste_chunks.py
# Move the cursor to the target window during the countdown.

import time
import sys
import pyautogui
import pyperclip

pyautogui.FAILSAFE = True  # move mouse to top-left to abort

# ----------------- CONFIG -----------------
FILENAME = "code.txt"         # file containing your code/text
START_DELAY = 5.0             # seconds to place cursor after starting the script
CHUNK_MAX_CHARS = 2000        # max characters per clipboard paste (adjust)
CHUNK_DELAY = 0.30            # seconds to wait between chunk pastes (adjust)
RESTORE_CLIPBOARD = True      # restore original clipboard when done
# ------------------------------------------

def read_lines(filename):
    with open(filename, "r", encoding="utf-8", errors="replace") as f:
        # splitlines() removes trailing newline characters — good for reconstructing chunks safely
        return f.read().splitlines()

def build_chunks(lines, max_chars):
    chunks = []
    cur = []
    cur_len = 0
    for line in lines:
        # +1 to account for the newline we will re-insert between lines
        need = len(line) + 1
        if cur and (cur_len + need) > max_chars:
            chunks.append("\n".join(cur))
            cur = []
            cur_len = 0
        cur.append(line)
        cur_len += need
    if cur:
        chunks.append("\n".join(cur))
    return chunks

def main():
    try:
        lines = read_lines(FILENAME)
    except FileNotFoundError:
        print(f"File not found: {FILENAME}")
        sys.exit(1)
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)

    original_clip = None
    if RESTORE_CLIPBOARD:
        try:
            original_clip = pyperclip.paste()
        except Exception:
            original_clip = None

    print(f"Read {len(lines)} lines from {FILENAME}.")
    chunks = build_chunks(lines, CHUNK_MAX_CHARS)
    print(f"Prepared {len(chunks)} chunk(s).")
    print(f"Place the cursor in the target window. Starting in {START_DELAY} seconds...")
    try:
        for i in range(int(START_DELAY), 0, -1):
            print(i, end=" ", flush=True)
            time.sleep(1)
        print("\nPasting... (move mouse to top-left to abort)")
        for idx, chunk in enumerate(chunks, start=1):
            pyperclip.copy(chunk)
            # short extra pause so OS clipboard updates reliably
            time.sleep(0.05)
            pyautogui.hotkey("ctrl", "v")
            # small delay to let the app process the pasted chunk
            print(f"  chunk {idx}/{len(chunks)} pasted")
            time.sleep(CHUNK_DELAY)
        print("All done.")
    except KeyboardInterrupt:
        print("\nInterrupted by user (KeyboardInterrupt).")
    except pyautogui.FailSafeException:
        print("\nAborted by mouse fail-safe (moved cursor to top-left).")
    finally:
        if RESTORE_CLIPBOARD and original_clip is not None:
            try:
                pyperclip.copy(original_clip)
            except Exception:
                pass

if __name__ == "__main__":
    main()
