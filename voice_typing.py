# Save as voice_typing.py (not speech_recognition.py!)
import speech_recognition as sr
import pyautogui
import time
import sys

def speech_to_text():
    try:
        recognizer = sr.Recognizer()
    except Exception as e:
        print(f"Error initializing recognizer: {e}")
        print("Make sure SpeechRecognition is installed: pip install SpeechRecognition")
        return

    try:
        mic = sr.Microphone()
    except Exception as e:
        print(f"Error accessing microphone: {e}")
        print("Check if microphone is connected and permissions are granted")
        return

    print("Adjusting for ambient noise... Please wait 2 seconds")
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
    except Exception as e:
        print(f"Error during noise adjustment: {e}")
        return

    print("Ready! Start speaking... (Press Ctrl+C to stop)")
    
    while True:
        try:
            with mic as source:
                print("\nListening...")
                audio = recognizer.listen(source, timeout=None)
                
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                    pyautogui.typewrite(text)
                    pyautogui.press("enter")
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand what you said")
                except sr.RequestError as e:
                    print(f"Could not request results; check your internet connection: {e}")
                    
        except KeyboardInterrupt:
            print("\nStopped by user")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

if __name__ == "__main__":
    print(f"Using Python at: {sys.executable}")
    print("Starting in 5 seconds... (Switch to your desired window)")
    time.sleep(5)
