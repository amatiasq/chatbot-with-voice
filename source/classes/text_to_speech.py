import pyttsx3


class SpeechModule:
    def __init__(self, lang, voice=0, volume=1, rate=125):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        lang_voices = [x for x in voices if lang in x.languages]

        for x in lang_voices:
            print(x)

        self.engine.setProperty("voice", lang_voices[voice].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
