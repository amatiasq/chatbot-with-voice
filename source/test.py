import speech_recognition as sr

r = sr.Recognizer()

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

with sr.Microphone(device_index=mic) as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    print('FOUND')

    try:
        text = r.recognize_google(audio, language="es")
        print('FOUND')
        print(text)
    except:
        print("Unexpected error:", sys.exc_info()[0])
