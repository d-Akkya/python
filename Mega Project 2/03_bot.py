import pyautogui
import pyperclip
import time

# Small delay to switch to the target window if needed
time.sleep(2)

# Step 1: Click on the edge icon at (646, 736)
pyautogui.click(646, 736)

# Step 2: Drag to select text from (499, 156) to (1320, 643)
pyautogui.moveTo(499, 156)
pyautogui.dragTo(1320, 643, duration=0.5, button='left')

# Step 3: Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')

# Step 4: Pause to ensure text is copied
time.sleep(0.5)

# Step 5: Retrieve the copied text from clipboard
text = pyperclip.paste()

print("Selected text:", text)