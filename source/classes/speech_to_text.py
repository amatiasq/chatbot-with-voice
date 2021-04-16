import speech_recognition as sr


def getValidMic():
    microphones = sr.Microphone.list_microphone_names()
    valid_mics = [x for x in microphones if "Microphone" in x]

    print("Microphones found ({0}):".format(len(microphones)))
    for index, name in enumerate(microphones):
        print("- Microphone(device_index={0}) for \"{1}\"".format(index, name))

    print("\nValid microphones ({0}):".format(len(valid_mics)))
    for name in valid_mics:
        print("- Valid \"{0}\"".format(name))

    mic = microphones.index(valid_mics[0])
    print("\nUsing \"{0}\" ({1})".format(microphones[mic], mic))

    return mic


mic_index = getValidMic()


class VoiceRecognitionModule:
    def __init__(self, lang):
        self.lang = lang
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone(device_index=mic_index) as source:
            print("Speak Anything: ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language=self.lang)
                return text
            except:
                return None
