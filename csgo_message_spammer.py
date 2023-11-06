import time
import pyautogui
def split_string(input_string, chunk_size):
    result = []

    for i in range(0, len(input_string), chunk_size):
        chunk = input_string[i:i + chunk_size]
        result.append(chunk)
    return result

def send_csgo_message(message):
    max_char = 2047
    pyautogui.hotkey('`')
    time.sleep(1)
    

    if len(message) >= 2047:
        message_list = split_string(message, max_char)
        for frac in message_list:
            pyautogui.typewrite(f'say {frac}')
            pyautogui.press('enter')
    else:
        pyautogui.typewrite(f'say {message}')
        pyautogui.press('enter')

    pyautogui.hotkey('`')