import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening.....")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if "curly bracket" in text:
            text = text.replace("curly bracket","\n{}")
        elif "circular bracket" in text:
            text = text.replace("circular bracket","()")
        elif "semi colon" in text:
            text = text.replace("semi colon",";")
        elif "colon" in text:
            text = text.replace("colon",":")

    except:
        pass