import pyttsx3
import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing.......")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data
        except sr.UnknownValueError:
            print("Sorry, could not understand.")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()




# Main program loop
while True:
    # Listen for user input
    user_input = sptext()

    # Process user input and respond
    if user_input.lower() == 'exit':
        print("Exiting program...")
        break
    elif user_input:
        speechtx("You said: " + user_input)
    else:
        speechtx("Sorry, could you please repeat that?")
        break

