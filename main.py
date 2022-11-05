import speech_recognition as sr
import time
import pyautogui
import pyperclip

mic = sr.Microphone() 
r = sr.Recognizer()

def callback(recognizer, audio):
    try:
        yazi = r.recognize_google(audio, language='tr-tr')
        if (yazi.startswith('yaz') and yazi.endswith("yaz")):
            yazi = yazi.replace("yaz","").strip()
            print(yazi)
            pyperclip.copy(yazi)
            pyautogui.hotkey("ctrl", "v")
        else:
            print(yazi)

    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")

r.listen_in_background(mic, callback)
while True: time.sleep(0.1)