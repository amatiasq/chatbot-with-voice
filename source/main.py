#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from classes.text_to_speech import SpeechModule
from classes.speech_to_text import VoiceRecognitionModule
from classes.chatbot_brain import ChatbotBrain


context = """who are you?
My name is Lorelei, I'm a robot from the future, I'm trapped \
in a Mac computer, I'm here to help the user of this computer"""

translation_artifacts_english = {"Disagreement": "Discord"}
translation_artifacts_spanish = {}


print("\n\n---\n\n")

chatbot = ChatbotBrain(
    context,
    translation_artifacts_english,
    translation_artifacts_spanish,
    "microsoft/DialoGPT-large",
    "microsoft/DialoGPT-large",
    True,
    True,
)


print("\n\n---\n\n")

speech = SpeechModule("es_ES", 1)
recognition = VoiceRecognitionModule('es')

print("\n\n---\n\n")


while True:
    text = recognition.recognize()
    print(text)

    if text:
        chatbot_text = chatbot.talk(text)
        print(chatbot_text)
        speech.talk(chatbot_text)
        # print(text)
        # speech.talk(text)
    else:
        print('nada')
        speech.talk("No te he entendido")
