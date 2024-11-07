import pyautogui
import pyperclip
import time
from openai import OpenAI

# Small delay to switch to the target window if needed
time.sleep(2)

# Step 1: Click on the edge icon at (646, 736)
pyautogui.click(691, 745)

while True:
    # Step 2: Drag to select text from (499, 156) to (1320, 643)
    pyautogui.moveTo(499, 156)
    pyautogui.dragTo(1320, 643, duration=0.5, button='left')

    # Step 3: Copy the selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(484, 201) # Deselect the text

    # Step 4: Pause to ensure text is copied
    time.sleep(0.5)

    # Step 5: Retrieve the copied text from clipboard
    chat_history = pyperclip.paste()

    print(chat_history)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a person named Akkya who speaks marathi as well as english. You are from India and you are a coder. You analyze chat history and respond like Akkya. Output should be the next chat response as Akkya"},
            {
                "role": "user",
                "content": chat_history
            }
        ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)

    # Step 6: Click at coordinates (1808, 1328)
    pyautogui.click(709, 693)
    time.sleep(1)  # Wait for 1 second to ensure the click is registered

    # Step 7: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

    # Step 8: Press Enter
    pyautogui.press('enter')